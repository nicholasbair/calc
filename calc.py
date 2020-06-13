import falcon
import pandas as pd

class AuthMiddleware(object):

  def process_request(self, req, resp):
    token = req.get_header('Authorization')

    if token is None:
      raise falcon.HTTPUnauthorized('Unauthorized')

    if not self._token_is_valid(token):
      raise falcon.HTTPUnauthorized('Unauthorized')

  def _token_is_valid(self, token):
    token == os.environ.get('CALC_TOKEN')


class Ema(object):

  def on_post(self, req, resp):
    df_test = pd.DataFrame(req.media['data'])
    df_test_ewma = df_test.ewm(alpha=0.1818).mean()

    resp.status = falcon.HTTP_200
    resp.body = (str(df_test_ewma.values.tolist()[-1][0]))

app = falcon.API(middleware=[
  AuthMiddleware()
])

ema = Ema()

app.add_route('/ema', ema)