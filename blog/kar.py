from kavenegar import *
class karn:
    """docstring for kar."""

    def __init__(self, number,ran):
        self.number = number
        self.ran = ran
    def ngar (self):
        try:
            api = KavenegarAPI('4A53745039504A3950553663614B774937516A6D4645354D4A594C71304674314A6D57717963516B466F303D')
            params = {
                'sender': '1000596446',#optional
                'receptor': self.number,#multiple mobile number, split by comma
                'message': self.ran,
            }
            response = api.sms_send(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)
