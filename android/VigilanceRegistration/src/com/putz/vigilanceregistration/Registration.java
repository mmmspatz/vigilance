package com.putz.vigilanceregistration;

import java.io.IOException;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;

import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.util.Log;

public class Registration extends Service {
	public int onStartCommand(Intent intent, int flags, int startId) {
		
		SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
		String endpoint = prefs.getString("host_name", "webcam.mit.edu/android");
		try {
			
			String descriptor = prefs.getString("device_description", "Invalid");
			HttpPost req = new HttpPost(endpoint);
			req.setEntity(new StringEntity(descriptor));
			requester.setRequest(req);
			Thread runner = new Thread(requester);
			runner.start();
			
		} catch (Exception e) {
			Log.d("Vigilance","Request failed " + endpoint);
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return 0;
	}
	
	@Override
	public IBinder onBind(Intent arg0) {
		
		
		return null;
	}	
	abstract class HttpRequester implements Runnable {
		public abstract void setRequest (HttpUriRequest req);
		public abstract void run();
	}
	HttpRequester requester = new HttpRequester() {
		HttpUriRequest hr;
		
		public synchronized void setRequest (HttpUriRequest req) {
			hr = req;
		}
		@Override
		public synchronized void run() {
			
			HttpClient httpc = new DefaultHttpClient();
			try {
				httpc.execute(hr);
				Log.d("Vigilance", "Request executed!");
			} catch (ClientProtocolException e) {
				Log.d("Vigilance", "Request failed!");
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				Log.d("Vigilance", "Request failed!");
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	};
}
