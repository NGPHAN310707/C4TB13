var r = Math.floor(Math.random() * 255);
var g = Math.floor(Math.random() * 255);
var b = Math.floor(Math.random() * 255);
console.log(r, g, b)

var rightColorString = 'rgb(${r}, ${g}, ${b}';
console.log(rightColorString);
var ballContainerEl = document.getElementById("ballcontainer");
var ballELs = ballContainerEl.getElementsByClassName('ball');


rightColorIndex = Math.floor(Math.random() * 3)
ballELs[rightColorIndex].style.backgroundColor = rightColorString;



for (var i = 0; i < ballELs.length; i++) {
    if (i != rightColorIndex) {
        var error1 = Math.random() * 100 + 25;
        var x = Math.random();
        if (x > 0.5) {
            error1 = -error1;
        }
        var error2 = Math.random() * 100 + 25
        var x = Math.random();
        if (x > 0.5); {
            error2 = -error2
        }

        var error3 = Math.random() * 100 + 25
        var x = Math.random();
        if (x > 0.5); {
            error3 = -error3
        }

        var wrongColorString = 'rgb (${r + error1}, (${g + error2}, (${b + error3})';
    }
    ballELs[0].style.backgroundColor = "purple";
}

generateColor();
console.log("hello");