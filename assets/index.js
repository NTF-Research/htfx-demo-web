




function recommend(event)
{
    if(event != null)
    {
        if( event.keyCode != 13)
            return
    }
    
    label_id = document.getElementById("category-box").value;
    text = document.getElementById("txt-search").value;
    if(text.length < 1)
        return

    fetch(`http://localhost:8000/recommend?label_id=${label_id}&text=${text}'`)
    .then(res => res.json())
    .then(data => {
        show_items(data)
    })
    .catch(err => console.log(err))
}

function recommend_by_category(event)
{
    label_id = event.target.id
    alert("recommend_by_category = " + label_id)
}

function recommend_by_histody()
{
    items = [1,2,3,4,5,6,7]
    show_items(items)
}

function init_category_box(categories)
{
    let html = '<option value="0">All</option>'
    categories.forEach(category => {
        html += `<option value="${category.id}">${category.name}</option>`
    });
    document.getElementById("category-box").innerHTML = html
}

function init_category_bar(categories)
{
    let html = '<span id="0" class="btn-category" onclick="recommend_by_category(event)">All</span>'
    categories.forEach(category => {
        html += `<span id="${category.id}" class="btn-category" onclick="recommend_by_category(event)">${category.name}</span>`
    });
    document.getElementById("nav-bottom").innerHTML = html
}

function show_items(items)
{
    let template = document.getElementById("item-template").innerHTML
    let html = ""
    items.forEach(item => {
        let item_html = template
        for (let key in item) {
            item_html = item_html.replaceAll(`{{${key}}}`, item[key]);
        }
        html += item_html
    })
    document.getElementById("item-container").innerHTML = html
}

window.onload = function()
{
    fetch('http://localhost:8000/categories')
    .then(res => res.json())
    .then(data => {
        init_category_box(data)
        init_category_bar(data)
    })
    .catch(err => console.log(err))

    recommend_by_histody()
}