// console.log('adfa');

// mapboxgl.accessToken = 'pk.eyJ1IjoiZmVlZGxpZ2h0NDIiLCJhIjoiY2xnY3d5eW92MTF3bzNjcWxvbm83enk4YyJ9.y2k3VZCUGo5cvYNEfDp7pA';
// var map = new mapboxgl.Map({
//           container: 'map',
//           style: 'mapbox://styles/feedlight42/clgqmxs0k00l501qxe6l42i05'
//         });





//  COLOR PALETTE


//  GREEN : #03C988
//  RED : #EB455F
//  ELLOW : #F9D949


//  TRIES for autocomplete
// 
// 

function makeNode(ch) {
  this.ch = ch;
  this.isTerminal = false;
  this.map = {};
  this.words = [];
}

function add(str, i, root) {

  if (i === str.length) {
      root.isTerminal = true;
      return;
  }

  if (!root.map[str[i]])
      root.map[str[i]] = new makeNode(str[i]);

  root.words.push(str);
  add(str, i + 1, root.map[str[i]]);
}

function search(str, i, root) {
  if (i === str.length)
      return root.words;

  if (!root.map[str[i]])
      return [];
  return search(str, i + 1, root.map[str[i]]);

}

const items = [
  "Marina Beach",
  "Kapaleeshwarar Temple",
  "Fort St. George",
  "Valluvar Kottam",
  "Santhome Basilica",
  "Guindy National Park",
  "Elliott's Beach",
  "Government Museum",
  "Theosophical Society",
  "Arignar Anna Zoological Park",
  "Vivekananda House",
  "Crocodile Bank",
  "Cholamandal Artists' Village",
  "DakshinaChitra",
  "Sri Parthasarathy Temple",
  "Kishkinta Theme Park",
  "MGR Film City",
  "Semmozhi Poonga",
  "Armenian Church",
  "VGP Universal Kingdom",
  "Kalakshetra Foundation",
  "Edward Elliot's Beach",
  "Pondy Bazaar",
  "Birla Planetarium",
  "Snake Park",
  "Ashtalakshmi Temple",
  "Valluvar Statue",
  "VGP Snow Kingdom",
  "Vandalur Zoo",
  "Ripon Building",
  "Sri Ramakrishna Math",
  "Anna Centenary Library",
  "Dheeran Chinnamalai Statue",
  "Connemara Public Library",
  "Chennai Rail Museum",
  "Government Estate",
  "Valluvar Kottam Monument"
];

const root = new makeNode('\0');
for (const item of items)
  add(item, 0, root);

const text_box = document.getElementById("get-source");
const list = document.getElementById("source-reco");

function handler(e) {
  const str = e.target.value;
  const predictions = search(str, 0, root);

  console.log(predictions);

  list.innerHTML = "";
  const a = 0;
  for (const prediction of predictions)

      // if( a === 5) { continue; }
      // list.innerHTML += `<li class="list-group-item clickable" onclick="handleClick(this)"><b>${str}</b>${prediction.substring(str.length)}</li>`;
      list.innerHTML += `<option><b>${str}</b>${prediction.substring(str.length)}</option>`
      console.log(list.innerHTML)



}

function handleClick(e) {
  text_box.value = e.innerText;
}

handler({ target: { value: "" } });


text_box.addEventListener("keyup", handler);

//  magnetic button

const butto = document.getElementById("get");

const btns = document.querySelectorAll(".btn");
    
        btns.forEach((btn) => {
          btn.addEventListener("mousemove", function(e){
            const position = btn.getBoundingClientRect();
            const x = e.pageX - position.left - position.width / 2;
            const y = e.pageY - position.top - position.height / 2;
    
            btn.children[0].style.transform = "translate(" + x * 0.3 + "px, " + y * 0.5 + "px)";
          });
        });
    
        btns.forEach((btn) => {
          btn.addEventListener("mouseout", function(e){
            btn.children[0].style.transform = "translate(0px, 0px)";
          });
        });




// end of mag button



//    MAP APGE

mapboxgl.accessToken = 'pk.eyJ1IjoiZmVlZGxpZ2h0NDIiLCJhIjoiY2xnY3d5eW92MTF3bzNjcWxvbm83enk4YyJ9.y2k3VZCUGo5cvYNEfDp7pA';
var map = new mapboxgl.Map({
  container: 'map',
//   style: 'mapbox://styles/mapbox/dark-v11',   //this is for the default themes
  //  style: 'mapbox://styles/feedlight42/clhmon4kn01qn01pghfyo88db', 
  style: 'mapbox://styles/mapbox/streets-v11',
  // center: [80.237617, 13.067439], // starting position [lng, lat]
  center: [80.11542, 12.89458],
  zoom: 10   // starting zoom
});

const input = document.getElementById("toggle");
console.log(input.checked);
console.log('wasss');

function toggle_dark()
{
    var checkbox = document.getElementById('toggle');

    if (checkbox.checked == true)
        {
            map.setStyle('mapbox://styles/mapbox/dark-v11');
            document.getElementById("header").className = 'header dark-header'
            document.getElementById("header_words").style = 'color: white;'
            document.getElementById("content").className = 'main-util dark-util'
            console.log(document.getElementById("header").className)
            document.getElementById("get").className = 'get-route-dark'
        }
    else 
        {
            map.setStyle('mapbox://styles/feedlight42/clhmon4kn01qn01pghfyo88db');
            document.getElementById("header").className = 'header light-header'
            document.getElementById("header_words").style = 'color: black;'
            document.getElementById("content").className = 'main-util light-util'
            console.log(document.getElementById("header").className)
            document.getElementById("get").className = 'get-route'
        }


}




// FUNCTIONALITY FOR THE FORM 

var form = document.getElementById('myForm');
var inputs = Array.from(form.getElementsByTagName('input'));
var getRouteButton = document.getElementById('get-route');

// validate inputs -- check if they're not empty

inputs.forEach(function(input){
  input.addEventListener('input', validateForm)
});

function validateForm() {
  var isFormValid = inputs.every(function(input){
    console.log(input.value);
    return input.value.trim() !== '';  
  });
  console.log(isFormValid);
  getRouteButton.disabled = !isFormValid;
}

form.addEventListener('submit', function(event){
  event.preventDefault(); // to prevent page from refreshing 

  var inputValues = inputs.map(function(input){
    console.log(input.value);
    return input.value;
  });

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/process_pathCoordinates', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        // Call a function to map the route in mapbox
        mapRoute(response);
      } else {
        console.log('Error::', xhr.status);
      }
  };
  xhr.send(JSON.stringify(inputValues));
});

function mapRoute(response){
  console.log('map is working routeing grig go');
  // remove source and layer if any 
  if (map.getSource('route')) {
    map.removeLayer('route');
    map.removeSource('route');
  }

  console.log(response);
  console.log('+++++++++++++++++++++++++++++++++++++++');

  var routeFeature = {
    type: 'Feature',
    properties: {},
    geometry: {
      type: 'LineString',
      coordinates: response
    }
  };

  map.addSource('route', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: [routeFeature]
    }
  });

  map.addLayer({
    id: 'route',
    type: 'line',
    source: 'route',
    paint: {
      'line-color': '#03C988',
      'line-width': 5
    }
  });

}











// // sample routing  code  
// map.on('load', () => {
//   map.addSource('route', {
//   'type': 'geojson',
//   'data': {
//   'type': 'Feature',
//   'properties': {},
//   'geometry': {
//   'type': 'LineString',
//   'coordinates': [[80.11542, 12.89458],
//                   [80.11581, 12.89457]],
//               }
//           }
//   });
//   map.addLayer({
//     'id': 'route',
//     'type': 'line',
//     'source': 'route',
//     'layout': {
//     'line-join': 'round',
//     'line-cap': 'round'
//     },
//     'paint': {
//     'line-color': '#4ad74a',
//     'line-width': 3
//     }
//     });
//     });

    // console.log('done');

