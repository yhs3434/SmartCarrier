package com.example.jjm.senierproject;

import android.content.Intent;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import org.json.JSONException;
import org.json.JSONObject;



public class Location extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_location);

        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        double latitude=0.0;
        double longitude=0.0;

        HttpGet httpGet = new HttpGet("http://yhs3434.pythonanywhere.com/gps/1");
        httpGet.start();
        try{
            httpGet.join();
        }catch(InterruptedException e){
            e.printStackTrace();
        }

        JSONObject gps = httpGet.getData();
        try {
            latitude = Double.parseDouble(gps.getString("latitude"));
            longitude = Double.parseDouble(gps.getString("longitude"));
        } catch (JSONException e) {
            e.printStackTrace();
        }

        // Add a marker in Sydney and move the camera
        LatLng myPlace = new LatLng(latitude, longitude);
        mMap.addMarker(new MarkerOptions().position(myPlace).title("Marker in myPlace"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(myPlace));
    }

}
