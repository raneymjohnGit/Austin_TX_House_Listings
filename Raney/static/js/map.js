
// Add console.log to check to see if our code is working.
console.log("working");

// read local JSON file in javascript
fetch("https://finalproject-04.s3.amazonaws.com/dataset.json")
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

  	var tbody = d3.select("tbody");
	tbody.html("");

	// Loop through the cities array and create one marker for each city.
	houseData.forEach(function(house) {
	console.log(house)
	let row = tbody.append("tr");

    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(house).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
    });

	// get table references
	
   	L.marker(house.location,
				  {radius : 10,
				  color: 'red' })
   .bindPopup("<h5>" + "City: " + house.city + "<br>" + "Zipcode: " + house.zipcode + "<br>" + "Lot Size SqFt: " + house.lotSizeSqFt +  "<br>" + "Living Area SqFt: " + house.livingAreaSqFt + "<br>" + "No Of Beds: " + house.numOfBedrooms + "<br>" + "No Of Baths: " + house.numOfBathrooms + "<br>" + "Average School Rating: " + house.avgSchoolRating +   "<br>" +  "Address: " + house.streetAddress + "</h5> <hr> <h4> Price: " + house.latestprice + "</h4>")
   .addTo(map)
  });

	// Then we add a control to the map that will allow the user to change which
	// layers are visible.
	L.control.layers(baseMaps).addTo(map);
  })







console.log("working");








