var gloser = {
  musikk:"música",
  naturfag:"ciencias naturales",
  gym:"educatión física",
  kunst:"artes",
  samfunnsfag:"ciencias sociales",
  historie:"historia",
  spansk:"español",
  matte:"matemáticas",
  relgion:"religión",
  språk:"idiomas",
  engelsk:"ingles",
  geografi:"geografía",
  barnehage:"guardería",
  barneskole:"colegio",
  vidergående:"instituto",
  universitet:"universidad",
  lære:"aprender",
  studere:"estudiar",
  skrive:"escribir",
  lese:"leer",
  jobbe:"trabajar",
  spiseFrokost:"desayunar",
  spiseLunsj:"almorzar",
  spiseMiddag:"cenar",
  våke:"despertarse",
  ståOpp:"levantarse",
  vaskeSeg:"lavarse",
  leggeSeg:"acostarse",
};

var totLen = Object.keys(gloser).length;
var currentWord;
var currentIndex;
var mode = "forced";
var keyValFirst = "keyFirst";
var outDiv = document.getElementById("main");
var wrongAnswers = [];
var totCorrect = 0;
var currentLen = Object.keys(gloser).length;

document.getElementById("startTest").onclick = function () {
  this.remove();
  var inp = document.createElement("INPUT");
  inp.placeholder = "Svar her";
  inp.id = "answer";
  inp.classList.add("text-input");
  inp.addEventListener("keyup", function (event) {
    if (event.keyCode === 13 && document.getElementById("answer").value == "") {
      event.preventDefault();
      if (document.body.style.backgroundColor == "limegreen") {
        next();
      } else {
        tryAgain();
      }
    } else if (event.keyCode === 13) {
      event.preventDefault();
      submitt();
    }
  });
  outDiv.append(inp);
  inp.onkeyup = function () {
    submitt;
  };
  document.getElementById("keyValFirst").remove();
  test(currentWord);
};

function submitt() {
  document.getElementById("submitt").remove();
  checkAnswer();
}

function test() {
  var button = document.createElement("button");
  button.innerHTML = "Submitt";
  button.id = "submitt";
  outDiv.append(button);
  if (mode == "random") {
    currentIndex = Math.floor(Math.random() * currentLen);
    console.log(currentIndex, currentLen);
  } else {
    currentIndex = 0;
  }
  if (keyValFirst == "keyFirst") {
    currentWord = Object.keys(gloser)[currentIndex];
    currentAnswer = Object.values(gloser)[currentIndex];
  } else {
    currentWord = Object.values(gloser)[currentIndex];
    currentAnswer = Object.keys(gloser)[currentIndex];
  }
  if (currentIndex < 0 || currentIndex > Object.keys(gloser).length) {
    return;
  }
  document.getElementById("submitt").onclick = function () {
    submitt();
  };
  var h1 = document.createElement("h1");
  h1.innerHTML = "Hva betyr " + currentWord + "?";
  outDiv.append(h1);
  outDiv.insertBefore(h1, outDiv.firstChild);
}

function checkAnswer() {
  var answer = document.getElementById("answer").value.toLowerCase();
  if (answer == currentAnswer) {
    document.body.style.backgroundColor = "limegreen";
    var button = document.createElement("BUTTON");
    button.setAttribute("onclick", "next()");
    button.innerHTML = "Next";
    button.id = "next";
    outDiv.append(button);
    totCorrect++;
    currentLen--;
    delete gloser[currentWord];
    delete gloser[currentAnswer];
  } else {
    document.body.style.backgroundColor = "red";
    var button = document.createElement("BUTTON");
    button.setAttribute("onclick", "tryAgain()");
    button.innerHTML = "Try again";
    button.id = "tryAgain";
    wrongAnswers.push(document.getElementById("answer").value);
    outDiv.append(button);
    alert(currentAnswer);
  }
  document.getElementById("answer").value = "";
}

function next() {
  document.body.style.backgroundColor = "white";
  var elements = document.querySelectorAll("h1");
  for (i = 0; i < elements.length; i++) {
    elements[i].remove();
  }
  document.getElementById("next").remove();
  if (totCorrect < totLen) {
    test();
  } else {
    endTest();
  }
}

function tryAgain() {
  document.body.style.backgroundColor = "white";
  var elements = document.querySelectorAll("h1");
  for (i = 0; i < elements.length; i++) {
    elements[i].remove();
  }
  document.getElementById("tryAgain").remove();
  test();
}

function endTest() {
  var div = outDiv.getElementsByTagName("*");
  for (i = 0; i < div.length; i++) {
    div[i].remove();
  }
  var h1 = document.createElement("H1");
  h1.innerHTML = "You are done";
  outDiv.append(h1);
  // var wAnswerStr = wrongAnswers.toString()
  var p = document.createElement("P");
  p.innerHTML =
    "You got " + wrongAnswers.length + " words wrong. These words were:";
  outDiv.append(p);
  var ul = document.createElement("ul");
  for (i = 0; i < wrongAnswers.length; i++) {
    var li = document.createElement("li");
    li.innerHTML = wrongAnswers[i];
    ul.append(li);
  }
  outDiv.append(ul);
}
