const images = ["1.jpg","2.jpg","3.jpg"];


const chosenimage = images[Math.floor(Math.random() * images.length)];

const bgimage = document.createElement("img");

bgimage.src=`image/${chosenimage}`;

document.body.appendChild(bgimage);