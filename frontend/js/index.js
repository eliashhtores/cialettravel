const renderDestinations = (destinations) => {
    var grid = document.getElementById("destinations-grid")
    if (!destinations.length) {
        grid.innerHTML = '<p class="text-slate-600">No destinations yet. Add one via the API.</p>'
        return
    }
    grid.innerHTML = destinations
        .map(function (d) {
            return (
                '<article class="card">' +
                '<h3 class="text-xl font-semibold">' +
                escapeHtml(d.name) +
                "</h3>" +
                '<p class="text-sm text-slate-600">' +
                escapeHtml(d.country) +
                "</p>" +
                '<p class="mt-2">' +
                escapeHtml(d.description) +
                "</p>" +
                "</article>"
            )
        })
        .join("")
}

const renderPackages = (packages) => {
    var grid = document.getElementById("packages-grid")
    if (!packages.length) {
        grid.innerHTML = '<p class="text-slate-600">No packages yet. Add one via the API.</p>'
        return
    }
    grid.innerHTML = packages
        .map(function (p) {
            return (
                '<article class="card">' +
                '<h3 class="text-xl font-semibold">' +
                escapeHtml(p.title) +
                "</h3>" +
                '<p class="text-sm text-slate-600">' +
                escapeHtml(p.destination_name) +
                " · " +
                escapeHtml(String(p.duration_days)) +
                " days" +
                "</p>" +
                '<p class="mt-2">' +
                escapeHtml(p.summary) +
                "</p>" +
                '<p class="mt-3 font-semibold text-indigo-700">$' +
                escapeHtml(String(p.price)) +
                "</p>" +
                "</article>"
            )
        })
        .join("")
}

const showError = (elementId, message) => {
    document.getElementById(elementId).innerHTML = '<p class="text-red-500">' + escapeHtml(message) + "</p>"
}

const escapeHtml = (str) => {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;")
}

const fetchJSON = (url, onSuccess, onError) => {
    var xhr = new XMLHttpRequest()
    xhr.open("GET", url)
    xhr.setRequestHeader("Accept", "application/json")
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            try {
                var data = JSON.parse(xhr.responseText)
                onSuccess(Array.isArray(data) ? data : data.results || [])
            } catch (e) {
                onError("Failed to parse response.")
            }
        } else {
            onError("Request failed with status " + xhr.status + ".")
        }
    }
    xhr.onerror = function () {
        onError("Network error.")
    }
    xhr.send()
}

fetchJSON("/api/destinations/", renderDestinations, function (msg) {
    showError("destinations-grid", msg)
})

fetchJSON("/api/packages/", renderPackages, function (msg) {
    showError("packages-grid", msg)
})
