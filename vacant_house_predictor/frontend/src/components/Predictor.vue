<template>
    <div class="container" style="text-align:center;">
    <div>
        <b-card
            :img-src="imageUrl"
            img-alt="Image"
            img-top
            style="width:600px;"
            tag="article"
            class="mb-2"
        >
            <!-- style="max-width: 20rem;" -->
            <b-card-text>
            住宅の外観画像を送信してください。
            </b-card-text>

            <b-button href="#" variant="outline-primary">Go somewhere</b-button>
        </b-card>
    </div>
    </div>
</template>

<script>
import noimage from "../assets/noimage.png";

export default {
    data() {
        return {
            imageUrl: noimage,
        }
    }
}
</script>

