package com.example.jjm.senierproject;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class Frame extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_frame);


        Button[] buttons = new Button[4];

        for(int i=0; i<4; i++) {
            int k= getResources().getIdentifier("btn" +(i+1),"id",getPackageName());
            buttons[i]= (Button)findViewById(k);
        }

        buttons[0].setText("NFC");
        buttons[1].setText("수동조작");
        buttons[2].setText("위치추적");
        buttons[3].setText("On / Off");


        Button.OnClickListener onClickListener = new Button.OnClickListener() {
            @Override
            public void onClick(View v) {
                Button button=(Button)v;
                if(v.getId()==R.id.btn1) {

                }
                if(v.getId()==R.id.btn2) {

                }
                if(v.getId()==R.id.btn3) {//클릭시 버튼 전환
                    Intent intent = new Intent(getApplicationContext(),Location.class);
                    startActivity(intent);
                    //finish(); // 현재 엑티비티를 없애고 다른 화면을 나타내기위해
                }
                if(v.getId()==R.id.btn4) {

                }
            }
        };

        for(int i=0; i<4; i++) {
            buttons[i].setOnClickListener(onClickListener);
        }
    }
}
