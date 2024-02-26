import { storedname } from "$lib/common";
import { get } from 'svelte/store'
console.log("layout server", get(storedname))
