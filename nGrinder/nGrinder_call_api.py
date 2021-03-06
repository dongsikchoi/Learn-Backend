# -- coding:utf-8 --
# A simple example using the HTTP plugin that shows the retrieval of a
# single page via HTTP.
#
# This script is automatically generated by ngrinder.
#
# @author dongsikchoi.dev
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from net.grinder.plugin.http import HTTPPluginControl
from java.util import Date
from HTTPClient import NVPair, Cookie, CookieModule
#from org.json import JSONObject
#from com.ibm.json.java import JSONObject
#import org.json.JSONObject;
import httplib
import urllib
import random 

#import requests
control = HTTPPluginControl.getConnectionDefaults()
# if you don't want that HTTPRequest follows the redirection, please modify the following option 0.
# control.followRedirects = 1
# if you want to increase the timeout, please modify the following option.
control.timeout = 6000
test1 = Test(1, "api.example.com")
#request1 = HTTPRequest()
# Set header datas
#headers = [] # Array of NVPair
#headers.append(NVPair("api-key", "api-key-example"))
#headers.append(NVPair("Content-Type", "application/json"))

#params = []
cookies = [] # Array of Cookie
class TestRunner:
	# initlialize a thread
	def __init__(self):
		test1.record(TestRunner.__call__)
		grinder.statistics.delayReports=True
		pass
	
	def before(self):
		#request1.headers = headers
		for c in cookies: CookieModule.addCookie(c, HTTPPluginControl.getThreadHTTPClientContext())
	# test method		
	def __call__(self):
		self.before()
		overall_list = [['country', 'AD', 'AE', 'AF', 'etc'], ['port'], ['product', 'tomcat', 'minecraft', 'etc'], ['favicon', '-12345678', '-222222' ,'etc'], ['cve_id', 'CVE-2022-01-01','etc'], ['after'], ['before'], ['keyword_example','login','RDP', 'etc']]
		keyword_index = random.randrange(0,2)
		keyword_element_index = random.randrange(0, len(overall_list[7]))
		list_index = random.randrange(0,7)

		if list_index == 1: # port case
			port = str(random.randrange(1,20001))
			port = ': '.join([overall_list[list_index][0],port])
			if keyword_index == 1:
				tmp_keyword = '"{}"'.format(overall_list[7][keyword_element_index])
				banner_keyword = ' '.join([tmp_keyword,port])
			else:
				banner_keyword = port

			print(banner_keyword)
		elif list_index == 5 or list_index == 6: # before or after case
			prefix = overall_list[list_index][0]
			year = str(random.randrange(2015,2023))
			month = str(random.randrange(1, 13))
			if len(month) < 2:
				month = '0' + month
			day = str(random.randrange(1, 32))
			if len(day) < 2:
				day = '0' + day
			target = year + '-' + month + '-' + day
			target = ': '.join([prefix,target])
			if keyword_index ==1:
				tmp_keyword = '"{}"'.format(overall_list[7][keyword_element_index])
				banner_keyword = ' '.join([tmp_keyword,target])

			else:
				banner_keyword = target
			print(banner_keyword)

		else:
			prefix = overall_list[list_index][0]
			element_index = random.randrange(1, len(overall_list[list_index]))
			target = ': '.join([prefix,overall_list[list_index][element_index]])
			if keyword_index ==1:
				tmp_keyword = '"{}"'.format(overall_list[7][keyword_element_index])

				banner_keyword = ' '.join([tmp_keyword,target])
			else:
				banner_keyword = target

			print(banner_keyword)


		print('##banner_keyword = ',banner_keyword)
		banner_keyword ='''{}'''.format(banner_keyword)
	
		
		params = urllib.urlencode({'search_text': banner_keyword, 'offset': 0, 'limit': 5,})

		headers = {'api-key':'api-key-sample'}
		
		url = '/api/location'

		conn = httplib.HTTPSConnection('api.example.com')
		conn.request('GET',url + params,"", headers)
		response = conn.getresponse()
		print('response status =',response.status)
		
		print('response result = ', response.read())
		print('##banner_keyword = ',banner_keyword)
		conn.close()

		if response.status == 200 :
			print('success')
			return
        
		else:
			grinder.logger.warn("Warning. The response may not be correct. The response code was %d." %  response.status)
			return