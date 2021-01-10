var AnimateLogo = function() {
  var tl, logo, letters, button, bg;
}

var _init = function() {
    logo    = document.getElementById('logo');
    button  = document.getElementById('restart');
    bg      = document.getElementById('bg');
    letters = document.getElementsByClassName('cfye__letter')
    letters = Array.prototype.slice.call(letters, 0);
    letters = letters.reverse();
    _addEventHandlers();
    _animate();
}

  var _addEventHandlers = function() {
    button.addEventListener('click', _play, false);
}

  var _animate = function () {
    tl = new TimelineLite();
    tl
      .staggerFromTo(letters, 0.4, {scale: 3, opacity:0, transformOrigin: 'center center'},{scale:1, opacity:1, ease:Back.easeOut}, 0.2)
      .to(bg, 0.4,{scale:1.2, transformOrigin: 'center',ease:Back.easeIn})
      .to(bg, 0.4,{scale:1, transformOrigin: 'center', ease:Bounce.easeOut})
    return tl;
  }

  var _play = function() {
    if (tl.progress() < 1) {
      tl.play();
    } else {
      tl.restart();
    }
    return {
      init: _init
    }();
  }
AnimateLogo.init();