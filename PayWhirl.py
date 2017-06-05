# PayWhirl API Python Library
#
# Use this library to interface with PayWhirl's API
# https://api.paywhirl.com
#
#  Example Usage:
#  =========================
#  $payWhirl = new \PayWhirl\PayWhirl($api_key,$api_secret);
#  $customer = $payWhirl->getCustomer($customer_id);
#
#

# Import python-requests
import requests
import json


class PayWhirl:


    # string The PayWhirl API key and secret to be used for requests.
    _api_key = ''
    _api_secret = ''

    # string The base URL for the PayWhirl API.
    _api_base = 'https://api.paywhirl.com'

    # Prepare to make request
    # @param string $api_key    Your Paywhirl API Key
    # @param string $api_secret Your PayWhirl API Secret
    def __init__(self, api_key, api_secret, api_base=False):
        # set API key and secret
        self._api_key = api_key
        self._api_secret = api_secret

        if api_base:
            self._api_base = api_base


    # Get a list of customers
    # @return Customer Array of Objects
    def getCustomers(self, data=[]):
        return self.get('customers', data)

    # *Get a customer
    # @param int $id Customer ID
    # @return Customer Object
    def getCustomer(self, cid):
        return self.get(str.format('/customer/{0}', cid))

    # Create a customer
    # @param int $data Customer data
    # @return Customer Object
    def createCustomer(self, data):
        return  self.post('/create/customer', data)

    # Update a customer
    # @param int $data Customer data
    # @return Customer Object
    def updateCustomer(self, data):
        return self.post('/update/customer',data)

    # Update a customer s answer toa profile questions
    # @param int $data Answer data
    # @return Answer Object
    def updateAnswer(self, data):
        return self.post('/update/answer', data)

    # Get a list of profile questions
    # @return Questions Array of Objects
    def getQuestions(self, data):
        return self.get('/questions', data)

    # Get a answers to a customer's questions
    # @return Answer Array of Objects
    def getAnswers(self, data):
        return self.get('/answers', data)

    # Get a list of plans
    # @return Plan Array of Objects
    def getPlans(self, data):
        return self.get('/plans', data)

    # Get a plan
    # @param int $id Plan ID
    # @return Plan Object
    def getPlan(self, id):
        return self.get('/plan/', id)

    # Create a plan
    # @param int $data Plan data
    # @return Plan Object
    def createPlan(self, data):
        return self.post('/create/plan', data)

    # Update a plan
    # @param int $data Plan data
    # @return Plan Object
    def updatePlan(self, data):
        return self.post('/update/plan', data)

    # Get a list of subscriptions for a customer
    # @param int $id Customer ID
    # @return Subscription List Object
    def getSubscriptions(self, id):
        return self.get('/subscriptions/', id)

    # Get a subscription
    # @param int $id Subscription ID
    # @return Subscription Object
    def getSubscription(self, id):
        return self.get('/subscription/'. id)

    # Get a list of active subscribers
    # @param array $data Array of options
    # @return Subscribers List
    def getSubscribers(self, data):
        return self.get('/subscribers', data)

    # Subscribe a customer to a plan
    # @param int $id Subscription ID
    # @return Subscription Object
    def subscribeCustomer(self, customer_id, plan_id,trial_end = False):
        data = [{
            'customer_id': customer_id,
            'plan_id': plan_id,
        }]

        if trial_end:
            data['trial_end'] = trial_end;

        return self.post('/subscribe/customer', data)

    # Subscribe a customer to a plan
    # @param int $id Subscription ID
    # @return Subscription Object
    def updateSubscription(self, subscription_id, plan_id):
        data = [{
            'subscription_id': subscription_id,
            'plan_id': plan_id,
        }]

        return self.post('/update/subscription', data)

    # Unsubscribe a Customer
    # @param int $id Subscription ID
    # @return Subscription Object
    def unsubscribeCustomer(self, subscription_id):
        data = [{
            'subscription_id': subscription_id,
        }]
        return self.post('/unsubscribe/customer', data)

    # Get a invoice
    # @param int $id Invoice ID
    # @return Invoice Object
    def getInvoice(self, id):
        return self.get('/invoice/', id)

    # Get a list of upcoming invoices for a customer
    # @param int $id Customer ID
    # @return Invoices Object
    def getInvoices(self, id):
        return self.get('/invoices/', id)

    # Get a list of payment gateways
    # @return Gateways Collection
    def getGateways(self):
        return self.get('/gateways')

    # Get a payment gateway
    # @param int $id Gateway ID
    # @return Gateway Object
    def getGateway(self, id):
        return self.get('/gateway/', id)

    # Create an invoice with a single charge
    # @param array $data data
    # @return Plan Object
    def createCharge(self, data):
        return self.post('/create/charge', data)

    # Get a charge
    # @param int $id Charge ID
    # @return Charge Object
    def getCharge(self, id):
        return self.get('/charge/', id)

    # Get a card
    # @param int $id Card ID
    # @return Gateway Object
    def getCard(self, id):
        return self.get('/card/', id)

    # Get a customer's cards
    # @param int $id Customer ID
    # @return Card List Object
    def getCards(self, id):
        return self.get('/cards/', id)

    # Create a card
    # @param array $data Card Data
    # @return Card Object
    def createCard(self, data):
        return self.post('/create/card', data)

    # Delete a card
    # @param int $id Card ID
    # @return boolean
    def deleteCard(self, id):
        data = [{'id': id}]
        return self.post('/delete/card', data)

    # Get a promo code
    # @param int $id Promo Code ID
    # @return Promo Code Object
    def getPromo(self, id):
        return self.get('/promo/', id)

    # Get an email template
    # @param int $id Email Template ID
    # @return Email Template Object
    def getEmailTemplate(self, id):
        return self.get('/email/', id)

    # Get authenticated account's information
    # @return PayWhirl account object
    def getAccount(self):
        return self.get('/account')

    # Get authenticated account's stats
    # @return PayWhirl account object
    def getStats(self):
        return self.get('/stats')

    # Get a shipping rule
    # @param int $id Shipping Rule ID
    # @return Shipping Rule Object
    def getShippingRule(self, id):
        return self.get('/shipping/', id)

    # Get a tax rule
    # @param int $id Tax Rule ID
    # @return Tax Rule Object
    def getTaxRule(self, id):
        return self.get('/tax/', id)

    # Get MultiAuth token
    # @param array $data Options
    # @return boolean
    def getMultiAuthToken(self, data):
        return self.post('/multiauth', data)

    # Send POST request
    def post(self, endpoint, params={}):
        url = self._api_base + '/' + endpoint
        headers = {'api_key': self._api_key, 'api_secret': self._api_secret}
        print(url, headers)
        resp = requests.post(url, headers=headers, params=params)
        ret = resp.json()
        resp.close()
        return ret

    # Send GET request
    def get(self, endpoint, params={}):
        #print(params)
        url = self._api_base + '/' + endpoint
        headers = {'api_key': self._api_key, 'api_secret': self._api_secret}
        print(url, headers)
        resp = requests.get(url, headers=headers, params=params)
        ret = resp.json()
        resp.close()
        return ret
