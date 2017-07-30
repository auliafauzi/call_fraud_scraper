import unittest
from IPython import embed
import os
import json

class ScraperApiTestCase(unittest.TestCase):

	def setUp(self):
		self.app = create_app(config_name="testing")
		self.client = self.app.test_client
		self.report = {'area_code': 404, 'comment': 'Fishing for personal data',
        			   'phone_number': '555-555-5555', 'number_of_reports': 3 }
		with self.app.app_context():
			db.create_all()			

def test_header_content_type:
	#assert application/json

def test_get_all_comments_none_exist(self):
	response = self.client().get('/callFraudScraper/reports')
	self.assertEqual(response.status_code, 200)
	#assert response body empty

def test_get_report_by_area_code_does_not_exist(self):
	response = self.client().get('/callFraudScraper/reports/areaCode/123')
	self.assertEqual(response.status_code, 404)
	#assert response body empty

def test_get_report_by_area_code_non_integer(self):
	response = self.client().get('/callFraudScraper/reports/areaCode/abc')
	self.assertEqual(response.status_code, 400)
	#assert response body empty	

def test_get_all_reports(self):
	response = self.client().post('/callFraudScraper', data=self.report)
	self.assertEqual(response.status_code, 201)
	response = self.client().get('/callFraudScraper/reports')
	self.assertEqual(response.status_code, 200)
	self.assertIn(self.report, str(response.data))

def test_get_report_by_area_code(self):
    response = self.client().post('/callFraudScraper/', data=self.report)
    self.assertEqual(response.status_code, 201)
    json_response = json.loads(response.data.decode('utf-8').replace("'", "\""))
    response = self.client().get(
          '/callFraudScraper/reports/areaCode/{}'.format(json_response['id']))
    self.assertEqual(response.status_code, 200)
    self.assertIn(self.report, str(response.data))