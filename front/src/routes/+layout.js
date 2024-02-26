import { storedname } from "$lib/common";
import { get } from 'svelte/store'
console.log("layout js", get(storedname))
let othername = ""
import { browser, building, dev, version } from '$app/environment';

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
    if (browser) {
        othername = localStorage["username"]
    }
    return {
        thename: get(storedname), othername
    };
}