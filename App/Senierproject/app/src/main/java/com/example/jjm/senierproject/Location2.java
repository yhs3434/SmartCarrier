package com.example.jjm.senierproject;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import org.json.JSONObject;

public class Location2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_location2);

        Intent intent = new Intent(this.getIntent());

        TextView text = (TextView)findViewById(R.id.text1);
        text.setText("123123");
    }
}
