import static net.grinder.script.Grinder.grinder
import static org.junit.Assert.*
import static org.hamcrest.Matchers.*
import net.grinder.script.GTest
import net.grinder.script.Grinder
import net.grinder.scriptengine.groovy.junit.GrinderRunner
import net.grinder.scriptengine.groovy.junit.annotation.BeforeProcess
import net.grinder.scriptengine.groovy.junit.annotation.BeforeThread
// import static net.grinder.util.GrinderUtils.* // You can use this if you're using nGrinder after 3.2.3
import org.junit.Before
import org.junit.BeforeClass
import org.junit.Test
import org.junit.runner.RunWith

import java.util.Date
import java.util.List
import java.util.ArrayList

import net.grinder.plugin.http.HTTPRequest
import net.grinder.plugin.http.HTTPPluginControl

import HTTPClient.Cookie
import HTTPClient.CookieModule
import HTTPClient.HTTPResponse
import HTTPClient.NVPair

// Uncomment this to use new experimental HTTP client.
// import org.ngrinder.http.HTTPRequest
// import org.ngrinder.http.HTTPResponse
// import org.ngrinder.http.cookie.Cookie
// import org.ngrinder.http.cookie.CookieManager

 // @author dongsikchoi.dev

@RunWith(GrinderRunner)
class TestRunner {

	public static GTest test
	public static HTTPRequest request
	public static NVPair[] headers = []
	public static NVPair[] params = []
	public static Cookie[] cookies = []

	@BeforeProcess
	public static void beforeProcess() {
		HTTPPluginControl.getConnectionDefaults().timeout = 300000
		test = new GTest(1, "example.com")
		request = new HTTPRequest()
		grinder.logger.info("before process.");
	}

	@BeforeThread
	public void beforeThread() {
		test.record(this, "test")
		grinder.statistics.delayReports=true;
		grinder.logger.info("before thread.");
	}

	@Before
	public void before() {
		request.setHeaders(headers)
		cookies.each { CookieModule.addCookie(it, HTTPPluginControl.getThreadHTTPClientContext()) }
		grinder.logger.info("before. init headers and cookies");
	}

	@Test
	public void test(){
	def random = new Random()
		params = [new NVPair("ip",(0..3).collect { random.nextInt(200) }.join('.'))]
		headers = [new NVPair("User-agent", "johndoe"), new NVPair("api-key","123456")]
		HTTPResponse result = request.GET("https://example.com/sample/location", params, headers)

        
		if (result.statusCode == 200) {
			assertThat(result.statusCode, is(200));
			
		} else {
			grinder.logger.warn("Warning. The response may not be correct. The response code was {}.", result.statusCode);
			
		}
		
		
	}
}
