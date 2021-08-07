
image = document.querySelector('.note')

// console.log(image)

// image.style.backgroundColor = "red"

// image.style.transform = 'rotate(-20deg)';

// image.style.padding = "50px 0px 0px 0px";


function moveRight() {

    image.style.transform = 'rotate(' + 10 + 'deg)';
    animate = setTimeout(moveRight,20);    // call moveRight in 20msec

 }
 function stop() {
    clearTimeout(animate);
    image.style.left = '100px'; 
}

 }

//  moveRight()
