export async function load({ cookies, url }) {
    console.log("layout-server", url.pathname)
    if (url.pathname != "/") {
        cookies.set("path", url.pathname, { path: '/' })

    }
    let username = cookies.get("username")
    let jwt = cookies.get("jwt")
    return { username, jwt }
}

