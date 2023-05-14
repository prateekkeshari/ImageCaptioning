function previewImage() {
    var imagePreview = document.getElementById("image_preview");
    var imageUrl = document.getElementById("image_url").value;
    if (imageUrl === "") {
      imagePreview.src = "https://images.pexels.com/photos/4452215/pexels-photo-4452215.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2";
    } else {
      imagePreview.src = imageUrl;
    }
  }
  
  function generateCaption() {
    var imageUrl = document.getElementById("image_url").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/generate");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  
    var captionDiv = document.getElementById("caption_div");
    captionDiv.innerHTML = "This GetYourGuide experience is an image of kayakers in a cave, surrounded by beautiful rock formations and illuminated by natural light. The kayakers are wearing life jackets and paddling in the crystal clear water. Book now on https://getyourguide.com.";
    captionDiv.classList.add("loading");
    captionDiv.classList.add("empty-state");
  
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        var response = JSON.parse(this.responseText);
        if (response && response.caption) {
          captionDiv.innerHTML = response.caption;
          captionDiv.classList.remove("empty-state");
        } else {
          captionDiv.innerHTML = "Failed to generate caption.";
        }
        captionDiv.classList.remove("loading");
      }
    }
  
    xhr.send("image_url=" + encodeURIComponent(imageUrl));
  }
  
  window.addEventListener("load", function() {
    previewImage();
  });
  