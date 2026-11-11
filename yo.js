// YosolosoY: cada letra se enciende junto a su gemela; el botón las cruza y el resultado es el mismo.
(function () {
  var p = document.getElementById("palabra");
  if (!p) return;
  var letras = p.querySelectorAll(".l");
  var reflejos = p.querySelectorAll(".r");
  var arcos = p.querySelectorAll(".arco");
  var reducir = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function apagar() {
    p.querySelectorAll(".on").forEach(function (e) { e.classList.remove("on"); });
  }
  function encender(i) {
    apagar();
    var k = Math.min(i, 8 - i);
    letras[i].classList.add("on");
    letras[8 - i].classList.add("on");
    if (k < 4 && arcos[k]) arcos[k].classList.add("on");
  }
  letras.forEach(function (el, i) {
    el.addEventListener("mouseenter", function () { encender(i); });
    el.addEventListener("focus", function () { encender(i); });
    el.addEventListener("click", function () { encender(i); });
  });
  p.addEventListener("mouseleave", apagar);
  p.addEventListener("focusout", apagar);

  // Entrada: los arcos se dibujan de afuera hacia adentro.
  if (!reducir) {
    p.classList.add("entra");
    var k = 0;
    var t = setInterval(function () {
      if (k > 3) { clearInterval(t); setTimeout(apagar, 500); return; }
      apagar(); encender(k); k++;
    }, 420);
  }

  // Botón: cada letra viaja hasta el lugar de su gemela. Se lee igual.
  var b = document.getElementById("reves");
  if (b) {
    b.addEventListener("click", function () {
      if (b.disabled) return;
      b.disabled = true;
      if (reducir) { setTimeout(function () { b.disabled = false; }, 600); return; }
      b.classList.add("gira");
      var cx = Array.prototype.map.call(letras, function (el) {
        var r = el.getBoundingClientRect(); return r.left + r.width / 2;
      });
      letras.forEach(function (el, i) {
        var t = "translateX(" + (cx[8 - i] - cx[i]) + "px)";
        el.style.transition = "transform .9s cubic-bezier(.65,0,.35,1)";
        el.style.transform = t;
        if (reflejos[i]) { reflejos[i].style.transition = el.style.transition; reflejos[i].style.transform = t; }
      });
      setTimeout(function () {
        letras.forEach(function (el) { el.style.transition = "none"; el.style.transform = ""; });
        reflejos.forEach(function (el) { el.style.transition = "none"; el.style.transform = ""; });
        b.classList.remove("gira");
        b.disabled = false;
      }, 950);
    });
  }
})();
