<script>
    import MemoryItem from "$lib/components/Content.svelte";
    import StarBG from "$lib/components/EmojiBackground.svelte"
  
    const memories = [
      {
        image: "/kidu/20240801_160245.jpg",
        text: "Hii kidammaa.... Ivathu ninn birthday🎊🎉... I wanted to do something special for you❤️❤️... adke ee website madide... ninnge ista aythu annkonthini... Idu memory hall anntha madini...",
      },
      {
        image: "/kidu/1677344538132.jpg",
        text: "To be you are beautiful as you are...🌍 ninu hinnge yavaglu khushi aage iruu... ee photo daag olle devi banndannge bandi 👀... ella devru ninna chanag nodkoli.. ",
      },
      {
        image: "/kidu/Kidufam.jpg",
        text: "Elladr kinntha munnche ninn family important... uncle aunty tamma ellru ninna channag nodkonndara... avr aashirvada yavaglu ninn mel irrli....",
      },
      {
        image: "/kidu/Kidufriends.jpg",
        text: "amele ninnge important irodu ninn bestiee friends... apoorva mathe aisiri✨.... avr yavaglu ninna chanag nodkonndara... ivaglu ninn khushige support madthara...✨.. Olle friends sikkyara ninnga..",
      },
      {
        image: "/kidu/MeAndKidu.jpg",
        text: "Amele nanu.... ninn fav 'idiot'... Nanu ninn well wisher....✨ mathe ninna yavaglu khushi aage nodkobek annod nann aase.... I will be always be with you whenever you need...❤️❤️",
      },
      {
        image: "/kidu/KiduFullFam.jpg",
        text: "Nimm family nijja tummba doddadu... addrallu ni ond tara ideal maglu nim famliy ge...✨. munnde nu ni hinnge channage.. nakkonntha ne iru...",
      },
      {
        image: "/kidu/KiduHairs.jpg",
        text: "Ninn udda kuddla nanng bhal issta..✨. nii sanna kudla ittkobeda.... udda kudla ne idu... adragge channda kanthi...",
      },
      {
        image: "/kidu/KiduGoat.jpg",
        text: "Ibbru avag ella mast maja maadivi.... snapchat naag ella filters hakkond mathadiddo mathadid...",
      },
      {
        image: "/kidu/LoveLetter.jpg",
        text: "Naa ninnga first letter bardiddu nenap aithi???... adanna aadre innomme oodu spelling mistakes bhal adav oppkonthini... aadra innomme please ooduu...",
      },
      {
        image: "/kidu/KiduFlower.jpg",
        text: "Na ninnga first bheti aadaga rose badlu Dasvala yak kotti anntha kelidyalla... ad yak anndra Dasvalakka 5 sections irthav.... preeti allu asste Trust, Respect, Honesty, Peace mathe Acceptance anntha 5 qualities bhal mukhya... adak kottidu..",
      },
      {
        image: "/kidu/KiduMallige.jpg",
        text: "Ninu avag ella update kodthiddi..... en madathi... en illa anntha.... adu nanngu bhal ista ithu",
      },
      {
        image: "/kidu/KiduAndMeInHeart.jpg",
        text: "Yella channage ithu.... nanu ninu ella khushi aage iddvi... aadr amel en aythu nanngu gothilla... mostly berevr enadru helidra antha.... adella bidu ivaga... but ni yavaglu alle irrthi...",
      },
      {
        image: "/kidu/KiduJadi.jpg",
        text: "Ni enara annko.... Nanng ni Jadi hakkonndre channda anasthi...",
      },
      {
        image: "/kidu/HubbyMaterial.jpg",
        text: "Howda... addr nang haag annsalla bidu...",
      },
      {
        image: "/kidu/KiduHiding.jpg",
        text: "Hannga innu est dina anntha kaddu kaddu nodi ninu???... Manas naag en aithi adan omme open aage hel ala... aa chotu manas naag innu en en hakkonthi....",
      },
      {
        image: "/kidu/KiduKaii.jpg",
        text: "Ninn kai hidiyaku addrusta beku.... nim relatives ella correct ee anndara.... ninna Kai todade muttbek.... asst channda adi ninuu....",
      },
      {
        image: "/kidu/KiduCringe.jpg",
        text: "En annde anntha feel aagbyada.... aadr ni cringe adi swalp",
      },
      {
        image: "/kidu/KiduFlower2.jpg",
        text: "Huvad kivige innonndu huvaa....",
      },
      {
        image: "/kidu/Jhumki.jpg",
        text: "Hannge roadside athva yavdara banngarad anngdi ge elladru hoodra enara ear-rings, Jhumuki or sara nodidra bare nina nenap aagthi... Adann nodidkudle baro first question... Id akin mel channda kanuthen anntha..",
      },
      {
        image: "/kidu/RaggingKidu.jpg",
        text: "Id nenap aithi ninnga? Idde iruth bid... yakanndra adrag naa adinii",
      },
      {
        image: "/kidu/KiduTraditional.jpg",
        text: "Ni traditional look naag nijja anndr nijja mast annasthii....",
      },
      {
        image: "/kidu/KiduPuttani.jpg",
        text: "Kidduu putaaniiiii!!!!!!!",
      },{
        image: "/kidu/RowdyKidu.jpg",
        text: "Rowdy baby?? alla alla rowdy kidammaa.....",
      },{
        image: "/kidu/CutieKidu.jpg",
        text: "Nang ee photo nijja bhal issta ayth..... nii hinnga photo haaktha iru.... pleaseeee",
      },
      {
        image: "/kidu/KiduFam2.jpg",
        text: "Innome family photo??",
      },
      {
        image: "/kidu/GobiKidu.jpg",
        text: "Gunndu Gunndu Kidamma",
      },
      {
        image: "/kidu/MehendiKidu.jpg",
        text: "Cutie patootie....",
      },
      {
        image: "/kidu/AvatarKidu.jpg",
        text: "Hinnga ond pose naag photo tagaskolana ommee.....",
      },
      {
        image: "/kidu/kiduWithCake.jpg",
        text: "Once again.... happy birthday kidammaaa..... nii yavaglu khushi aag nakkonntha irruuu..... ee varsha niii annkonndidduuuuu ellaaaaa aagllliiiii.......",
      },
    ];
  </script>
  <StarBG floatemoji="⭐" emoji="✨"/>
  <main class="memory-page">
    <br>
    <h1 class="title">💖 Memory Hall 💖</h1>
  
    <div class="memory-container">
      {#each memories as memory}
        <MemoryItem image={memory.image} text={memory.text} />
      {/each}
    </div>
  </main>
  
  <style>
    .memory-page {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      min-height: 100vh;
      background: rgba(255, 182, 193, 0.3);
    }
  
    .title {
      font-size: 2.5rem;
      font-weight: bold;
      color: #ff69b4;
      margin-bottom: 20px;
    }
  
    .memory-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 75%; /* Match Content.svelte */
  max-width: 1100px; /* Allow it to be wider */
}

  
    @media (max-width: 768px) {
      .title {
        font-size: 2rem;
      }
    }
  </style>
  