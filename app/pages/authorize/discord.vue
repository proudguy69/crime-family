<template>
    you are being redirected, please wait
</template>

<script setup lang="ts">
import type UserInformation from '~/types/UserInformation'
import {authorizeDiscord} from '~/utils/authorize'

// varibles
const route = useRoute()
const router = useRouter()
const code = route.query.code as string

const api_uri = inject<Ref>('api_uri')!
const user_information = inject<Ref<UserInformation>>('user_information')!

// methods
onMounted(async () => {
    // console.log(api_uri.value)
    // if (!api_uri.value) {return}
    const result = await authorizeDiscord(code, api_uri.value, user_information)
    if (result) {
        console.log("auth failed?", result)
    }
    router.push('/')
})

</script>