
import logging
from textblob import TextBlob
import twily_classifier as cl
#import stop_words as stopwords
import json
from pathlib import Path
import os.path
import pathlib
import random
import nltk
nltk.download('punkt')


bot_host =str()
#STOP_WORDS = stopwords.sw_list
neg_distribution = []
pos_distribution = []
user_input_polarity = 0
user_input_subjectivity = 0


#This will load the persona script
def load_startup_persona_file(startup_file):
    my_directory = pathlib.Path().absolute()
    my_directory = os.path.join(str(my_directory), "personas")
    startup_file = os.path.join(my_directory, startup_file)
    with open(startup_file, 'r') as f:
        persona_data = json.load(f) 
    return(persona_data)

def load_next_persona(persona_data, personas_in_directory_list,	current_persona_number):
    starting_persona_file = personas_in_directory_list[current_persona_number]
    persona_data = load_startup_persona_file(starting_persona_file)
    bot_host = random.choice(persona_data["jackalbot_hosts"])   #set host from random list      
    logging.info('introduction:Start of session')
    startup_info = {k: persona_data[k] for k in ('jackalbot_name', 'jackalbot_created',  'jackalbot_updated', 'jackalbot_version', 'jackalbot_author', 'jackalbot_hosts', 'intro_prompt', 'jackalbot_score_to_move_to_next_stage', 'jackalbot_num_guess_then_offer_clue', 'jackalbot_num_guess_max_then_move_on')}
    logging.info('session info:%s' % startup_info)
    # Set global varribles
    conversation_phase  = 'needs'
    past_show_scores = False
    total_score_dictionary = {} #initialize global varrible before giving it to a function
    total_score_dictionary["did_it_sound_like_nvc_pos"]         = 0.00
    total_score_dictionary["input_polarity"]                    = 0.00
    total_score_dictionary["input_subjectivity"]                = 0.00
    total_score_dictionary["input_response_score"]              = 0.00
    total_score_dictionary["cleaned_did_it_sound_like_nvc_pos"] = 0.00
    total_score_dictionary["cleaned_input_polarity"]            = 0.00
    total_score_dictionary["cleaned_input_subjectivity"]        = 0.00
    total_score_dictionary["cleaned_input_response_score"]      = 0.00
    persona_data["show_scores"] = False
    bot_response = f"------------------------------------- <br><br>"  + persona_data["intro_prompt"] 
    return bot_response, persona_data

def look_for_keyword(user_input, persona_data):
    #check for NVC help
    response = ""
    user_input = ' '.join(user_input)  # to convert from list to string
    if user_input == 'nvc help' : response = "Type &#39;nvc needs&#39; to see the list." #
    if user_input == 'nvc' : response = "Type &#39;nvc_needs&#39; to see the list." #
    #if user_input == 'nvc feelings' : response =  persona_data["feelings_list"]
    if user_input == 'nvc needs' : response =  persona_data["needs_list"] 
    #if user_input == 'nvc end' : response =  "This feature is not ready yet"   # exit() 
    if user_input == 'nvc clue' : response =  persona_data["needs_clue"] 
    if user_input == 'nvc scores' : 
        persona_data["show_scores"] = not persona_data["show_scores"]
        response =  f'Show scores set to {persona_data["show_scores"]}'
    if user_input == 'nvc next' : response =  "This feature is not ready yet" 
    if user_input == 'nvc set' : response =  "This feature is not ready yet" 
    if user_input == 'set hungry' : response =  "This feature is not ready yet" 
    return response

def did_it_sound_like_nvc(u_input):
    """Utilitarian function: Appends 'neg_distribution'
    with negative probability, returns Negative Probability"""

    blob_it = cl.trainer().prob_classify(u_input)
    npd = round(blob_it.prob("neg"), 5)
    neg_distribution.append(npd)
    ppd = round(blob_it.prob("pos"), 5)
    pos_distribution.append(ppd)
    nvc_relevance_score = [npd, ppd]
    return npd,ppd

def main_conversation_corpus(user_input, conversation_data):
    """Rule base bot, takes an argument, user input in form of a string.  In sequence will pre-process the string. Lower case, tokenize and remove  stop words. iterates through CONVERSATION, if filtered_input intersects  response_set is updated. if the set is empty, it returns a message,    else it returns the longest string in the set"""
    try: 
        highest_number_of_matching_words = 0
        number_of_matching_words = []
        response_set = set()
        if conversation_data == 'none' : return "","" 
        for con_list in conversation_data:
            sentence = con_list[0]
            response = con_list[1]
            score = con_list[2]
            sentence_split = sentence.split()
            number_of_matching_words = set(user_input).intersection(sentence_split)
            if len(number_of_matching_words) > highest_number_of_matching_words:
                highest_number_of_matching_words = len(number_of_matching_words)
                best_response = response
                best_score = score
                
        if highest_number_of_matching_words == 0:
            return "," , 0
        else:
            return best_response, best_score
    except:
        raise Exception        

def get_response_from_user_and_clean(user_input, conversation_phase, persona_data) :

        #set conversation data to correct one
    if conversation_phase=="intro"    : stop_words = persona_data["intro_conversations_stop_words"]
    if conversation_phase=="feelings" : stop_words = persona_data["feelings_conversations_stop_words"]
    if conversation_phase=="needs"    : stop_words = persona_data["needs_conversations_stop_words"]
    if conversation_phase=="strategy" : stop_words = persona_data["strategy_conversations_stop_words"]

    # convert to text_blob  
    cleaned_user_input = TextBlob(user_input)
    # lowercase   
    cleaned_user_input = cleaned_user_input.lower()

    # remove stop words
    token_input = cleaned_user_input.words
    cleaned_user_input = [w for w in token_input if w not in stop_words]

    # lematize - not yet
      
    return cleaned_user_input

def make_response(cleaned_user_input, user_input,  conversation_phase, persona_data, english_bot):
    # if look_for_keyword
    key_word_found = look_for_keyword(cleaned_user_input, persona_data)
    if key_word_found: 
        bot_response = key_word_found
        bot_status = "key word found"
        response_score = 0
        return "System Information: " + bot_response, bot_status, response_score
    
    #set conversation data to correct one
    if conversation_phase=="intro"    : conversation_data = persona_data["intro_conversation_data_examples"]
    if conversation_phase=="feelings" : conversation_data = persona_data["feelings_conversation_data_examples"]
    if conversation_phase=="needs"    : conversation_data = persona_data["needs_conversation_data_examples"]
    if conversation_phase=="strategy" : conversation_data = persona_data["strategy_conversation_data_examples"]

    # check in main phase_corpus
    in_main_corpus, response_score = main_conversation_corpus(cleaned_user_input, conversation_data)
    if in_main_corpus != "," : # This is in the main corpus so get a response
        bot_response = in_main_corpus
        bot_status = "found in main corpus"

    if in_main_corpus == "," :  #not in main corpus, 
        user_resposne_string =  user_input  # set to orginal   OR  ' '.join(cleaned_user_input)  # make a string
        #  #set conversation data to correct one
        if conversation_phase=="intro"    : general_bot_support_prompts = persona_data["intro_general_bot_support_prompts"]
        if conversation_phase=="feelings" : general_bot_support_prompts = persona_data["feelings_general_bot_support_prompts"]
        if conversation_phase=="needs"    : general_bot_support_prompts = persona_data["needs_general_bot_support_prompts"]
        if conversation_phase=="strategy" : general_bot_support_prompts = persona_data["strategy_general_bot_support_prompts"]

        bot_response = general_bot_support_prompts  # 
        #bot_response = str(english_bot.get_response(user_resposne_string)) # + "\n\r" +  str(persona_data["intro_general_bot_support_prompts"])  # response and the re-direct
        if len(bot_response):
            bot_status = "sent to general bot"
        else:
            bot_response= "I did not understand your comment. Please try again" 
            bot_status = "no answer"   

        response_score = 0

    return bot_host + "  "+bot_response, bot_status, response_score

def do_scoring_and_logging(user_input, cleaned_user_input, bot_status, response_score, total_score_dictionary):
    cleaned_user_input = TextBlob(str(cleaned_user_input))
    user_input = TextBlob(str(user_input))
    logging.info('user_input: %s' % str(user_input))

    #set varribles
    user_input_did_it_sound_like_nvc={"did_it_sound_like_nvc": did_it_sound_like_nvc (user_input)}
    (sound_like_nvc_pos, sound_like_nvc_neg) = did_it_sound_like_nvc (user_input)
    user_input_polarity={"input_polarity": user_input.polarity}
    user_input_subjectivity={"input_subjectivity": user_input.subjectivity}
    user_input_response_score={"input_response_score": response_score}
    
    #write user input scores
    user_input_response_scores = str(user_input_did_it_sound_like_nvc)+", "+str(user_input_polarity)+", "+str(user_input_subjectivity)+", "+str(user_input_response_score)
    logging.info(
        'user_input_response_scores: %s' % user_input_response_scores)

    #total_score_dictionary["did_it_sound_like_nvc_pos"] = total_score_dictionary["did_it_sound_like_nvc_pos"] + sound_like_nvc_pos
    #total_score_dictionary["input_polarity"]        = total_score_dictionary["cleaned_input_polarity"]         + user_input.polarity
    #total_score_dictionary["input_subjectivity"]    = total_score_dictionary["cleaned_input_subjectivity"]    + user_input.subjectivity
    #total_score_dictionary["input_response_score"]  = total_score_dictionary["cleaned_input_response_score"]  + response_score


    #This function will only return the scores for the cleaned_user_input
    cleaned_user_input_did_it_sound_like_nvc={"did_it_sound_like_nvc", did_it_sound_like_nvc (cleaned_user_input)}
    (cleaned_sound_like_nvc_pos, cleaned_sound_like_nvc_neg) = did_it_sound_like_nvc (cleaned_user_input)
    cleaned_user_input_polarity={"input_polarity", cleaned_user_input.polarity}
    cleaned_user_input_subjectivity={"input_subjectivity", cleaned_user_input.subjectivity}
    cleaned_user_input_response_score={"input_response_score", response_score}

    cleaned_user_input_response_scores = str(cleaned_user_input_did_it_sound_like_nvc)+", "+str(cleaned_user_input_polarity)+", "+str(cleaned_user_input_subjectivity)+", "+str(cleaned_user_input_response_score)
    logging.info('cleaned_user_input: %s' % str(cleaned_user_input))
    logging.info(
        'cleaned_user_input_response_scores: %s' % cleaned_user_input_response_scores)

    #total_score_dictionary["cleaned_did_it_sound_like_nvc_pos"] = total_score_dictionary["cleaned_did_it_sound_like_nvc_pos"] + cleaned_sound_like_nvc_pos
    #total_score_dictionary["cleaned_input_polarity"]        = total_score_dictionary["cleaned_input_polarity"]         + cleaned_user_input.polarity
    #total_score_dictionary["cleaned_input_subjectivity"]    = total_score_dictionary["cleaned_input_subjectivity"]    + cleaned_user_input.subjectivity
    #total_score_dictionary["cleaned_input_response_score"]  = total_score_dictionary["cleaned_input_response_score"]  + response_score

    return cleaned_user_input_response_scores, total_score_dictionary  #this only sends the cleaned vers

def create_game_state_dictionary (personas_in_directory_list, current_persona_number, conversation_phase, past_show_scores, bot_host,  persona_data, game_state_dictionary) :
    game_state_dictionary['personas_in_directory_list'] = personas_in_directory_list
    game_state_dictionary['current_persona_number'] = current_persona_number
    game_state_dictionary['conversation_phase'] = conversation_phase
    game_state_dictionary['past_show_scores'] = past_show_scores
    game_state_dictionary['bot_host'] = bot_host
    game_state_dictionary['persona_data'] = persona_data

    # save file
    session_directory = pathlib.Path().absolute()
    session_directory = os.path.join(str(session_directory), "session")
    file_name = 'session.json'    
    session_file_path = os.path.join(session_directory, file_name)
    with open(session_file_path, 'w') as f:
        json.dump(game_state_dictionary, f)

    return 
    
def read_game_state_dictionary_into_varribles (game_state_dictionary):

    # save file
    session_directory = pathlib.Path().absolute()
    session_directory = os.path.join(str(session_directory), "session")
    file_name = 'session.json'    
    session_file_path = os.path.join(session_directory, file_name)
    with open(session_file_path, 'r') as f:
        game_state_dictionary = json.load(f) 

    personas_in_directory_list = game_state_dictionary['personas_in_directory_list']
    current_persona_number = game_state_dictionary['current_persona_number']
    conversation_phase = game_state_dictionary['conversation_phase']
    past_show_scores =game_state_dictionary['past_show_scores']
    bot_host = game_state_dictionary['bot_host']
    persona_data   = game_state_dictionary['persona_data']    
    return personas_in_directory_list,	current_persona_number, conversation_phase, past_show_scores, bot_host, persona_data 




def jackalbot_response (user_input):
    global english_bot # Not used at this time 
    english_bot  = 1 # not used now
    global game_state_dictionary
    game_state_dictionary={} # initialize

    if user_input in ["yy", "start", "Yy", "Start"]   :    #startmg a new game
        # get the first file_in_personas_folder
        #my_directory = r'personas/'
        #entries = Path(my_directory) #get sorted list of file items
        
        app_dir_path = pathlib.Path().absolute()  # get app path
        my_directory = os.path.join(str(app_dir_path), "personas")   # add persona to it
        entries = Path(my_directory) #get sorted list of file items
        personas_in_directory_list = []
        for entry in entries.iterdir():
            personas_in_directory_list.append(entry.name)  # put the nemes in a list
        current_persona_number = 0    #set to 0 to start at begining of list
        starting_persona_file = personas_in_directory_list[current_persona_number]
        persona_data = load_startup_persona_file(starting_persona_file)

        bot_host = random.choice(persona_data["jackalbot_hosts"])   #set host from random list      
        logging.info('introduction:Start of session')
        startup_info = {k: persona_data[k] for k in ('jackalbot_name', 'jackalbot_created',  'jackalbot_updated', 'jackalbot_version', 'jackalbot_author', 'jackalbot_hosts', 'intro_prompt', 'jackalbot_score_to_move_to_next_stage', 'jackalbot_num_guess_then_offer_clue', 'jackalbot_num_guess_max_then_move_on')}
        logging.info('session info:%s' % startup_info)
        # Set global varribles
        conversation_phase  = 'needs'
        past_show_scores = False
        total_score_dictionary = {} #initialize global varrible before giving it to a function
        total_score_dictionary["did_it_sound_like_nvc_pos"]         = 0.00
        total_score_dictionary["input_polarity"]                    = 0.00
        total_score_dictionary["input_subjectivity"]                = 0.00
        total_score_dictionary["input_response_score"]              = 0.00
        total_score_dictionary["cleaned_did_it_sound_like_nvc_pos"] = 0.00
        total_score_dictionary["cleaned_input_polarity"]            = 0.00
        total_score_dictionary["cleaned_input_subjectivity"]        = 0.00
        total_score_dictionary["cleaned_input_response_score"]      = 0.00

        persona_data["show_scores"] = False
        bot_response = f"---------STARTING  NEW SESSION ------------------- <br><br>"  + persona_data["intro_prompt"] 

        #save game state
        
        create_game_state_dictionary (personas_in_directory_list, current_persona_number, conversation_phase, past_show_scores, bot_host,  persona_data, game_state_dictionary)
        return bot_response

    if user_input in ["begin", "b"]    :  #tart the next session
        
        #load values from game_state_dictionary
        personas_in_directory_list, current_persona_number, conversation_phase, past_show_scores, bot_host,  persona_data = read_game_state_dictionary_into_varribles (game_state_dictionary)

        try :
            current_persona_number = current_persona_number + 1    #set to 1 to start at begining of list
        except :
            bot_response = f"-------------------Enter &#39;start&#39; to play.-------------------"
            return bot_response
        
        if current_persona_number == len(personas_in_directory_list) :  #if on last item
            bot_response = f"------------------------------------- <br>"  +"This is the end of the session.  Enter &#39;start&#39; to play again."
            return bot_response
        else :
            bot_response, persona_data = load_next_persona(persona_data, personas_in_directory_list, current_persona_number) 

            #save game state
        create_game_state_dictionary (personas_in_directory_list, current_persona_number, conversation_phase, past_show_scores, bot_host,  persona_data, game_state_dictionary)
        return bot_response



    if  user_input not in ["begin", "b", "B", "Begin", "yy", "start", "Yy", "Start"]  : #if a normal statement

        #load values from game_state_dictionary
        personas_in_directory_list, current_persona_number, conversation_phase, past_show_scores, bot_host,  persona_data = read_game_state_dictionary_into_varribles (game_state_dictionary)
        total_score_dictionary = {}
        try:
            if conversation_phase == 'test'  :  #intro Phase
                x=2 # should throw an error on the first time that is caught by the except block
        except:
            bot_response = "System: When you are ready type 'start' in the text box below." 
            return bot_response  # wait for user to type  'nvc start'
        if conversation_phase == 'intro'  :  #intro Phase
            cleaned_user_input = get_response_from_user_and_clean(user_input, conversation_phase, persona_data )
            bot_response, bot_status, response_score =  make_response(cleaned_user_input, user_input, conversation_phase, persona_data, english_bot)
            scoring_response, total_score_dictionary = do_scoring_and_logging(user_input, cleaned_user_input, bot_status, response_score, total_score_dictionary )
            if response_score == 100: 
                conversation_phase = 'feelings'   # Level achieved, move to next stage
        elif conversation_phase== 'feelings'  :  #Feeling Phase
            cleaned_user_input = get_response_from_user_and_clean(user_input,  conversation_phase, persona_data )
            bot_response, bot_status, response_score =  make_response(cleaned_user_input, user_input, conversation_phase, persona_data, english_bot)
            scoring_response, total_score_dictionary = do_scoring_and_logging(user_input, cleaned_user_input, bot_status, response_score, total_score_dictionary )
            if response_score == 100: 
                conversation_phase = 'needs'  # Level achieved, move to next stage
        elif conversation_phase == 'needs' :  #Needs Phase
            cleaned_user_input = get_response_from_user_and_clean(user_input,  conversation_phase, persona_data)
            bot_response, bot_status, response_score =  make_response(cleaned_user_input, user_input, conversation_phase, persona_data, english_bot)
            scoring_response, total_score_dictionary = do_scoring_and_logging(user_input, cleaned_user_input, bot_status, response_score, total_score_dictionary )
            if response_score == 100: 
                conversation_phase = 'needs'    #strategy'  # stay in loop for needs in this case
        elif conversation_phase == 'strategy' :  #Strategy Phase
            cleaned_user_input = get_response_from_user_and_clean(user_input,  conversation_phase, persona_data )
            bot_response, bot_status, response_score =  make_response(cleaned_user_input, user_input,  conversation_phase, persona_data, english_bot)
            scoring_response, total_score_dictionary = do_scoring_and_logging(user_input, cleaned_user_input, bot_status, response_score, total_score_dictionary )
            if response_score == 100: 
                conversation_phase = 'end'  # Level achieved, move to next stage
        
        if persona_data["show_scores"] == True  and past_show_scores == True : 
            #bot_response = bot_response+ "\n\r" + scoring_response  
            bot_response = "<font size='1'><b> System scores (last statement):</b> " + scoring_response  + " <br> </b>System scores (totals): </b>" + str(total_score_dictionary) +  "</font> To toggle off type: nvc scores <br>" + " <br>" + bot_response
            #bot_response = r'<p style="font-size:12px"> System scores : ' + scoring_response  + r'</p><br>' +  r' <br>' + bot_response
        elif persona_data["show_scores"] == True  and past_show_scores == False : 
            bot_response = bot_response 
            past_show_scores = True        
        elif persona_data["show_scores"] == False : 
            bot_response = bot_response 

        #save game state
        create_game_state_dictionary (personas_in_directory_list, current_persona_number, conversation_phase, past_show_scores, bot_host,  persona_data, game_state_dictionary)
        return bot_response


