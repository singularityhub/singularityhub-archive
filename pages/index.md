---
layout: page
title: Singularity Hub Archive
permalink: /
---

{% include card-style.html %}

# Welcome to Singularity Hub Archive!

Find a collection by name here, or use the search _at the top of the site or sidebar_ for more advanced recipe search.
 <div id="search">
   <div class="input-group">
     <div class="form-outline">
       <input placeholder="search" type="search" id="searchbox" class="form-control" />
     </div>
   </div>
 </div>
<main class="grid flex-grid" id='app'>{% for collection in site.collection %}
  <div onclick='document.location="{{ site.baseurl }}{{ collection.url }}"' class='card'>{{ collection.full_name }}</div>
{% endfor %}</main> 

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
$("#searchbox").on("keyup", function () {
    var search = $(this).val().trim().toLowerCase();
    $('.card').hide();
    $(".card").show().filter(function () {
        return $(this).text().toLowerCase().indexOf(search) < 0;
    }).hide();        
});
</script>
