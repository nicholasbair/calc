import falcon
import pandas as pd

class ema(object):

  def on_post(self, req, resp):
    df_test = pd.DataFrame(req.media['data'])
    df_test_ewma = df_test.ewm(alpha=0.1818).mean()

    resp.status = falcon.HTTP_200
    resp.body = (str(df_test_ewma.values.tolist()[-1][0]))

app = falcon.API()

ema = ema()

app.add_route('/ema', ema)