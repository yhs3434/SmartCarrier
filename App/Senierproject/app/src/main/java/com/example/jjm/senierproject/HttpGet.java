package com.example.jjm.senierproject;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class HttpGet extends Thread {
    URL url;
    JSONObject data;

    public HttpGet(String url_string){
        try {
            this.url = new URL(url_string);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        data = null;
    }

    @Override
    public void run(){
        HttpURLConnection conn = null;
        try {
            conn = (HttpURLConnection) url.openConnection();

            InputStream in = new BufferedInputStream(conn.getInputStream());
            data = new JSONObject(getStringFromInputStream(in));

        } catch (IOException e) {
            e.printStackTrace();
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    private static String getStringFromInputStream(InputStream is) {
        BufferedReader br = null;
        StringBuilder sb = new StringBuilder();

        String line;
        try {
            br = new BufferedReader(new InputStreamReader(is));
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return sb.toString();
    }


    public JSONObject getData(){
        return data;
    }
}
