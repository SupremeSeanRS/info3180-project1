function change(){
    document.getElementById('proPic').click()
}

document.getElementById('proPic').onchange = uploadOnChange;

function uploadOnChange() {
  var filename = this.value;
  var lastIndex = filename.lastIndexOf("\\");
  if (lastIndex >= 0) {
    filename = filename.substring(lastIndex + 1);
  }
  document.getElementById('upImg').innerHTML = filename;
}