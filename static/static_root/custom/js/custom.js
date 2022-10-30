// Get the Scroll button
let mybutton = document.getElementById("scrollBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        mybutton.style.display = "block";
    }
    else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
// Slick animation
$(document).ready(function () {
    $('.single-item').slick({
        dots: true,
        arrows: true,
    });
});

// My Resume Filter.
function AddClass(element, name) {
    let arr1;
    arr1 = element.className.split(" ");
    if (arr1.indexOf(name) == -1) {
        element.className += " " + name;
    }
}
function RemoveClass(element, name) {
    let arr1;
    arr1 = element.className.split(" ");
    const index = arr1.indexOf(name);
    if (index > 0) {
        arr1.splice(index, 1);
    }
    element.className = arr1.join(" ");
}
const resumeFilter = (props) => {
    const educationSection = document.getElementsByClassName('educationSection');
    const experienceSection = document.getElementsByClassName('experienceSection');
    const skillSection = document.getElementsByClassName('skillSection');

    const name = 'd-none'
    if (props === 'experienceSection') {
        RemoveClass(experienceSection[0], name);
        AddClass(skillSection[0], name);
        AddClass(educationSection[0], name);
    }
    else if (props === 'skillSection') {
        RemoveClass(skillSection[0], name);
        AddClass(experienceSection[0], name);
        AddClass(educationSection[0], name);
    }
    else if (props === 'educationSection') {
        RemoveClass(educationSection[0], name);
        AddClass(experienceSection[0], name);
        AddClass(skillSection[0], name);
    }
}
// AOS Anitialize
AOS.init({
    duration: 1500,
    delay: 200,
});




