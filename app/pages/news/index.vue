<template>
    <UContainer>
        <UPageHeader title="Famiglia Sangue News"/>
        Bellow you'll find all our news articles
    </UContainer>
    
    <UPageSection>
        <UPageCard title="All news articles" class="bg-gray-700/75 border-gray-50/25 border">
            <UBlogPosts :posts="posts" orientation="vertical" />
        </UPageCard>
    </UPageSection>
</template>

<script setup lang="ts">
import type { BlogPostProps } from '@nuxt/ui';


const posts = ref<BlogPostProps[]>([
    {
        title: 'Governor brings cad to departments',
        image: '/images/governordispatcher.png',
        description: "Phoenix City takes a major step forward in public safety as Governor Mal officially rolls out a brand-new Computer-Aided Dispatch (CAD) system, modernizing how the city's emergency services communicate and respond. In this exclusive interview with Phoenix City News, the Governor breaks down what the new system means for law enforcement, first responders, and the community at large.",
        to: '/news/article/1',
        date: '03/19/26',
        badge: "Exclusive interview!",
        authors: [
            {
                name: '[Don] Giacomo Daniele',
                description: '@orangegreencat',
                avatar: {
                    src: 'https://tr.rbxcdn.com/30DAY-AvatarHeadshot-D6224FA5661672A46609171666DFC0EE-Png/150/150/AvatarHeadshot/Png/noFilter'
                }
            }
        ]
    },
])

</script>