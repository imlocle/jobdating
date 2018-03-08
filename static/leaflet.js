var myMap = L.map("map", {
    center: [45.52, -122.67],
    zoom: 26
    });

// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." +
  "T6YbdDixkOBWH_k9GbS8JQ"
).addTo(myMap);

// for loop to create a list of store locations
var cities = [{
    location: [40.7128, -74.0059],
    name: "New York",
    population: "8,550,405"
  },
  {
    location: [41.8781, -87.6298],
    name: "Chicago",
    population: "2,720,546"
  },
  {
    location: [29.7604, -95.3698],
    name: "Houston",
    population: "2,296,224"
  },
  {
    location: [34.0522, -118.2437],
    name: "Los Angeles",
    population: "3,971,883"
  },
  {
    location: [41.2524, -95.9980],
    name: "Omaha",
    population: "446,599"
  }
];

  for (var i = 0; i < cities.length; i++) {
    var city = cities[i];
    L.marker(city.location)
      .bindPopup("<p>" + city.name + "</p> <hr> <p>Population " + city.population + "</p>")
      .addTo(myMap);
  }