const API_KEY = 'c740ad8da89250e0f6232bb14328c9d3'

function onGeoOk(position){
    const lat=position.coords.latitude;
    const lng=position.coords.longitude;
    const url =`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`
    fetch(url).then(response => response.json().then(data=> {
        const name=data.name;
        const weather=data.weather[0].main
    )});
}
function onGeoError(){
    alert("Can't find you. No weather for you.");

}



navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError);