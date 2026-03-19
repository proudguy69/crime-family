<template>
    <UPageSection v-if="article">
        <UPageCard variant="subtle" class="bg-gray-900/75 border-gray-50/25 border" :ui="{header: 'w-full'}">
            <template #header class="w-full" >
                <div class="flex items-center justify-between w-full">
                    <div class="flex items-center gap-2 bg-gray-950 p-2 rounded-md">
                        <UAvatarGroup>
                            <UAvatar size="xl" src="https://cdn.discordapp.com/avatars/1267552151454875751/8a9584069302bc80962cc9e4dab99c84.webp"/>
                            <UAvatar class="bg-gray-950" size="xl" src="https://tr.rbxcdn.com/30DAY-AvatarHeadshot-D6224FA5661672A46609171666DFC0EE-Png/150/150/AvatarHeadshot/Png/noFilter"/>
                        </UAvatarGroup>
                        <div class="flex flex-col">
                            <span class="font-bold text-lg">[Don] Giacomo Daniele</span>
                            <span class="font-light">@orangegreencat</span>
                        </div>
                    </div>

                    <span class="bg-gray-950 rounded-md p-1 flex flex-col h-full items-center">
                        <span>Thursday</span>
                        <span class="bg-gray-900/75 rounded-sm px-1">Mar 19, 2026</span>
                    </span>
                    
                </div>
                
            </template>
            <ContentRenderer :value="article"/>
        </UPageCard>
    </UPageSection>
   
    <div v-else>not found</div>
</template>

<script setup lang="ts">

const { data: article } = await useAsyncData(() => queryCollection('content').path('/articles/1').first())
</script>