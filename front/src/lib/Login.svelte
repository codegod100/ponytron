<script>
    import {storedname, create_user} from "$lib/common"
    export let logged_in = false;
    export let username = $storedname
    let password = ""

    console.log("we got", username)
    if(username){
        logged_in = true
    }
</script>
{#if !logged_in}
Hello: {username}
    <form
        on:submit|preventDefault={async () => {
            storedname.set(username)
            await create_user({username,password})
            logged_in = true
        }}
    >
        Username
        <input bind:value={username} type="text" />
        Password
        <input bind:value={password} type="text" />
        <button>login</button>
    </form>
{:else}
Hello {username} <button on:click={()=>{
    logged_in = false
    storedname.set("")
}}>logout</button>
{/if}
<div>&nbsp;</div>