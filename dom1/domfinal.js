// var el = document.getElementById("btn_search");
// console.log(el);
// var rects = document.getElementsByClassName("rects");
// console.log(rects);
// for (var i = 0; i < rects.length; i++) {
//     console.log(rects[i]);
// }

// var divs = document.getElementsByTagName("div");
// for (var i = 0; i < divs.length; i++) {
//     console.log(divs[i]);
// }

var a = document.getElementById("song_container");
console.log(a);
var b = a.getElementsByClassName("song");
console.log(b);

for (var i = 0; i < b.length; i++) {
    var c = b[i].getElementsByClassName('title');
    var d = b[i].getElementsByClassName('artist');
}
// var del = a.getElementsByTagName('button');
// console.log(del);
// for (var i = 0; i < del.length; i++) {
//     var pop = del[i];
//     pop.addEventListener('click', function(e) {
//         var btn = e.target;
//         var div = btn.parentNode;
//         div.remove();
//     });
// }
// var edit = a.getElementsByClassName('button');
// console.log(edit);
// for (var i = 0; i < edit.length; i++) {
//     var edits = edit[i];
//     edits.addEventListener('click', function(r) {
//         var btn = r.target;
//         var div = btn.parentNode;
//         console.log(div);
//     })
// }
// var more = a.getElementsByClassName('button');
// console.log(more);
// for (var i = 0; i < more.length; i++) {
//     var mores = more[i];
//     mores.addEventListener('click', function(t) {
//         var btn = t.target;
//         var div = btn.parentNode;
//         var c = div.getElementsByClassName('title');
//         var d = div.getElementsByClassName('artist');
//         console.log(c, d);
//     });
// }

var buttons = a.getElementsByTagName('button');
for (let index = 0; index < buttons.length; index++) {
    const element = buttons[index];
    if (element.innerHTML == 'Delete') {

    } else if (element.innerHTML == 'Edit') {


    }
}
var edit = a.getElementsByClassName('button');
console.log(edit);
for (var i = 0; i < edit.length; i++) {
    var edits = edit[i];
    edits.addEventListener('click', function(r) {
        var btn = r.target;
        var div = btn.parentNode;
        console.log(div);
    })
}