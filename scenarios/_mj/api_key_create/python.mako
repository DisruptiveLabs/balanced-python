% if mode == 'definition':
balanced.APIKey

% elif mode == 'request':
import balanced

balanced.configure('ak-test-1kvvievk0Qqw5wQPsrlM9g7wQwNe62cyc')

api_key = balanced.APIKey()
api_key.save()
% endif