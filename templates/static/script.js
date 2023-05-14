function previewImage() {
  var imagePreview = document.getElementById("image_preview");
  var imageUrl = document.getElementById("image_url").value;
  if (!validateImageUrl(imageUrl)) {
    imageUrl = defaultImageUrl;
  }

  imagePreview.src = imageUrl;
}


function generateCaption() {
  var imageUrl = document.getElementById("image_url").value;
  var captionDiv = document.getElementById("caption_div");

  // Reset previous error message
  captionDiv.innerHTML = "";
  captionDiv.classList.remove("error");

  // Perform image URL validation
  if (!validateImageUrl(imageUrl)) {
    captionDiv.innerHTML = "Oops 😥! That looks like an invalid image URL. Supported images are .jpg, .jpeg, and .png.";
    captionDiv.classList.add("error");
    captionDiv.classList.remove("generated"); // Remove generated state class
    return;
  }

  // Proceed with generating caption
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/generate");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  captionDiv.innerHTML = "Generating caption...";
  captionDiv.classList.add("loading");
  captionDiv.classList.remove("generated"); // Remove generated state class

  xhr.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE) {
      if (this.status === 200) {
        var response = JSON.parse(this.responseText);
        if (response && response.caption) {
          captionDiv.innerHTML = response.caption;
          captionDiv.classList.add("generated"); // Apply generated state class
          captionDiv.classList.remove("error"); // Remove error state class
        } else {
          captionDiv.innerHTML = "Failed to generate description.";
          captionDiv.classList.remove("generated"); // Remove generated state class
          captionDiv.classList.add("error"); // Apply error state class
        }
      } else {
        captionDiv.innerHTML = "Error generating description.";
        captionDiv.classList.remove("generated"); // Remove generated state class
        captionDiv.classList.add("error"); // Apply error state class
      }
      captionDiv.classList.remove("loading");
    }
  }

  xhr.send("image_url=" + encodeURIComponent(imageUrl));
}

function validateImageUrl(imageUrl) {
  // Perform image URL validation logic
  // Customize this regular expression based on your specific requirements
  var imageExtensions = /\.(jpeg|jpg|png|gif)(\?|$)/i;
  return imageExtensions.test(imageUrl);
}

window.addEventListener("load", function() {
  previewImage();
});
