from vendored.ask import alexa


def handler(request_obj, context=None):
    """
    This is the main function to enter to enter into this code.
    If you are hosting this code on AWS Lambda, this should be the entry point.
    Otherwise your server can hit this code as long as you remember that the
    input 'request_obj' is JSON request converted into a nested python object.
    """

    metadata = {'user_name': 'SomeRandomDude'}

    ''' inject user relevant metadata into the request if you want to, here.
    e.g. Something like :
    ... metadata = {'user_name' : some_database.query_user_name(request.get_user_id())}
    Then in the handler function you can do something like -
    ... return alexa.create_response('Hello there {}!'.format(request.metadata['user_name']))
    '''
    return alexa.route_request(request_obj, metadata)


@alexa.default_handler()
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return alexa.create_response(message="Just ask", end_session=True)


@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Hello Welcome to Ask Shrugs!", end_session=True)


@alexa.request_handler("SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)


@alexa.intent_handler('AMAZON.HelpIntent')
def help_intent_handler(request):
    message = "Let's face it, you're bad at making decisions. " \
              "Simply ask shrugs what should I do, and I'll tell you what to do." \
              "You can also ask what game should I play, what should I watch, " \
              "and soon, what should I eat or where should I go to eat."
    return alexa.create_response(message=message, end_session=True)


@alexa.intent_handler('WhatShouldIDo')
def next_recipe_intent_handler(request):
    from random import choice
    options = [
        "play a game",
        "watch netflix",
        "go for a walk",
        "go for a hike"
    ]
    pre = "You should "
    selected_option = choice(options)
    return alexa.create_response(message="{} {}".format(pre, selected_option), end_session=True)


@alexa.intent_handler('WhatShouldIWatch')
def next_recipe_intent_handler(request):
    from random import choice
    options = [
        "archer",
        "good eats",
        "futurama",
        "james bond",
        "rick and morty"
    ]
    pre = "You should "
    selected_option = choice(options)
    return alexa.create_response(message="{} {}".format(pre, selected_option), end_session=True)


@alexa.intent_handler('WhatGame')
def next_recipe_intent_handler(request):
    from random import choice
    options = [
        "netrunner",
        "netrunner but this time be the corporation faction",
        "pandemic",
        "firefly",
        "smash up",
        "galaxy trucker",
        "dominos (maybe at lucky 13)"
    ]
    pre = "You should play"
    selected_option = choice(options)
    return alexa.create_response(message="{} {}".format(pre, selected_option), end_session=True)
