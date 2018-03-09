var myMap = L.map("map", {
    center: [33.7747511, -118.4590902],
    zoom: 6
    });

// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
  "T6YbdDixkOBWH_k9GbS8JQ"
).addTo(myMap);


// d3.json('/companyjson', function(data){
//   for (var i = 0; i < data.length; i++){
//     var city = data[i];
//     L.marker(city.location)
//       .bindPopup("<p>" + city.name + "</p>")
//       .addTo(myMap);
//   }
// });
// for loop to create a list of store locations

var cities = [{
  company: "Indeed.com",
  lat_lon: [30.2672, -97.7431],
  city:   "Austin, TX",
  match: "85%"
},
{
  company:     "Costco",
  lat_lon:       [47.5301, -122.0326],
  city: "Issaquah, WA",
  match: "74%"
},
{
  company:     "Google",
  lat_lon:       [37.7749, -122.4194],
  city: "San Francisco, CA",
  match: "89%"
},
{
  company:     "Lakers",
  lat_lon:       [33.9165781, -118.4373346],
  city: "El Segundo, CA",
  match: "99%"
}
];


// var cities = [{
//     location: [40.7128, -74.0059],
//     name: "New York",
//     population: "8,550,405"
//   },
//   {
//     location: [41.8781, -87.6298],
//     name: "Chicago",
//     population: "2,720,546"
//   },
//   {
//     location: [29.7604, -95.3698],
//     name: "Houston",
//     population: "2,296,224"
//   },
//   {
//     location: [34.0522, -118.2437],
//     name: "Los Angeles",
//     population: "3,971,883"
//   },
//   {
//     location: [41.2524, -95.9980],
//     name: "Omaha",
//     population: "446,599"
//   }
// ];

  for (var i = 0; i < cities.length; i++) {
    var city = cities[i];
    L.marker(city.lat_lon)
      .bindPopup("<p>Name: " + city.company + "</p><br><p>City: "+ city.city + "</p><br><p>Match Rate: " + city.match +"</p>")
      .addTo(myMap);
  }



  //hello is it me youre looking for?
  // I can see it in your eyes

  