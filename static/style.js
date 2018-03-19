d3.json('/companyjson', function(data){
  console.log(data);
  var myMap = L.map("map", {
            center: [33.7747511, -118.4590902],
            zoom: 6 });

  L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" + "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." + "T6YbdDixkOBWH_k9GbS8JQ"
  ).addTo(myMap);
  
  for (var i = 0; i < data.length; i++){
    console.log(data[i]);
    L.marker(data[i].lat_lon)
      .bindPopup(`<p>Name: ${data[i].company}<br>Distanced Away: ${data[i].distance_away}</p>`)
      .addTo(myMap);
  }
});

