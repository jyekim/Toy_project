let speech = new SpeechSynthesisUtterance();

let voices = [];

let voiceSelect = document.querySelector("select");

//구글번역 넣는거?
window.speechSynthesis.onvoiceschanged = () => {
    voices = window.speechSynthesis.getVoices();
    speech.voice = voices[0]; 

    voices.forEach((voice, i) => (voiceSelect.options[i] = new Option(voice.name, i)));
};

//default 보이스 지정하기 
voiceSelect.addEventListener("change", () =>{
    speech.voice = voices[voiceSelect.value];
});

document.querySelector("button").addEventListener("click", () =>{
    speech.text = document.querySelector("textarea").value;
    window.speechSynthesis.speak(speech)
});