
// Add console.log to check to see if our code is working.
console.log("working");

// read local JSON file in javascript
fetch("static/js/dataset.js")
  .then(function (response) {
    return response.json();
  })
  .then(function (houseData) {
    
	// We create the tile layer that will be the background of our map.
	let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

	// Create the map object with center, zoom level and default layer.
	let map = L.map('mapid', {
	center: [30.267153, -97.7430608],
	zoom: 11,
	layers: [streets]
});

	// We create the second tile layer that will be the background of our map.
	let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

// Create a base layer that holds all three maps.
	let baseMaps = {
	"Streets": streets,
	"Satellite": satelliteStreets
  };

	// Loop through the cities array and create one marker for each city.
	houseData.forEach(function(house) {
	console.log(house)
   	L.marker(house.location,
				  {radius : 10,
				  color: 'red' })
   .bindPopup("<h2>" + "City = " + house.city + "<br>" + "zipcode = " + house.zipcode + "<br>" + "SqFt = " + house.livingAreaSqFt +  "<br>" + "No Of Baths = " + "<br>" + house.numOfBathrooms +  "<br>" +  "Address = " + house.streetAddress + "</h2> <hr> <h3> Price = " + house.latestPrice + "</h3>")
   .addTo(map)
  });

	// Then we add a control to the map that will allow the user to change which
	// layers are visible.
	L.control.layers(baseMaps).addTo(map);
  })







console.log("working");








