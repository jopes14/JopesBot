import discord
from discord.ext import commands
async def GetCharactersNames(ctx: discord.AutocompleteContext):
    return ['Baby Peach', 'Baby Daisy', 'Baby Rosalina', 'Lemmy', 'Baby Mario', 'Baby Luigi', 'Dry Bones', 'Light Mii', 'Toadette', 'Wendy', 'Isabelle', 'Koopa Troopa', 'Lakitu', 'Bowser Jr.', 'Toad', 'Shy Guy', 'Larry', 'Cat Peach', 'Inkling Girl', 'Female Villager', 'Peach', 'Daisy', 'Yoshi', 'Birdo', 'Tanooki Mario', 'Inkling Boy', 'Male Villager', 'Mario', 'Ludwig', 'Medium Mii', 'Luigi', 'Iggy', 'Rosalina', 'King Boo', 'Link', 'Metal Mario', 'Gold Mario', 'Pink Gold Peach', 'Waluigi', 'Donkey Kong', 'Roy', 'Wario', 'Dry Bowser', 'Bowser', 'Morton', 'Heavy Mii']
async def GetKartsNames(ctx: discord.AutocompleteContext):
    return ['Standard Kart', 'The Duke', '300 SL Roadster', 'Pipe Frame', 'Varmint', 'City Tripper', 'Mach 8', 'Sports Coupe', 'Inkstriker', 'Steel Driver', 'Tri-Speeder', 'Bone Rattler', 'Cat Cruiser', 'Teddy Buggy', 'Comet', 'Yoshi Bike', 'Circuit Special', 'B-Dasher', 'P-Wing', 'Badwagon', 'GLA', 'Standard ATV', 'Prancer', 'Sport Bike', 'Jet Bike', 'Biddybuggy', 'Mr Scooty',' Landship', 'Streetle', 'Sneaker', 'Gold Standard', 'Master Cycle', 'W 25 Silver Arrow', 'Standard Bike', 'Flame Rider', 'Wild Wiggler', 'Blue Falcon', 'Splat Buggy', 'Tanooki Kart', 'Koopa Clown', 'Master Cycle Zero']
async def GetWheelsNames(ctx: discord.AutocompleteContext):
    return ['Standard', 'Blue Standard', 'GLA Tires', 'Monster', 'Hot Monster', 'Ancient Tires', 'Roller', 'Azure Roller', 'Slim', 'Wood', 'Crimson Slim', 'Slick', 'Cyber Slick', 'Metal', 'Gold Tires', 'Button', 'Leaf Tires', 'Off-Road', 'Retro Off-Road', 'Triforce Tires', 'Sponge', 'Cushion']
async def GetGlidersNames(ctx: discord.AutocompleteContext):
    return ['Super Glider', 'Waddle Wing', 'Hylian Kite', 'Cloud Glider', 'Parachute', 'Flower Glider', 'Paper Glider', 'Wario Wing', 'Plane Glider', 'Gold Glider', 'Paraglider', 'Peach Parasol', 'Parafoil', 'Bowser Kite', 'MKTV Parafoil']
CharacterData = {
    'Baby Peach':{'Speed':2.5,'MiniTurbo':4.5,'Emojii':'<:MK8_BabyPeach_Icon:1126298586724978739>'},
    'Baby Daisy':{'Speed':2.5,'MiniTurbo':4.5,'Emojii':'<:MK8_BabyDaisy_Icon:1126298527891472504>'}, 
    'Baby Rosalina':{'Speed':2.5,'MiniTurbo':4.5,'Emojii':'<:MK8_BabyRosalina_Icon:1126298587907764307>'}, 
    'Lemmy':{'Speed':2.5,'MiniTurbo':4.5,'Emojii':'<:MK8_Lemmy_Icon:1126298681818222683>'}, 
    'Baby Mario':{'Speed':2.75,'MiniTurbo':4.5,'Emojii':'<:MK8_BabyMario_Icon:1126298585852547112>'}, 
    'Baby Luigi':{'Speed':2.75,'MiniTurbo':4.5,'Emojii':'<:MK8_BabyLuigi_Icon:1126298584736862332>'}, 
    'Dry Bones':{'Speed':2.75,'MiniTurbo':4.5,'Emojii':'<:MK8DX_Dry_Bones_Icon:1126298981648044182>'}, 
    'Light Mii':{'Speed':2.75,'MiniTurbo':4.5,'Emojii':'<:Mii_MK8:1126298535449595935>'}, 
    'Toadette':{'Speed':3,'MiniTurbo':4.25,'Emojii':'<:MK8_Toadette_Icon:1126298896902131752>'}, 
    'Wendy':{'Speed':3,'MiniTurbo':4.25,'Emojii':'<:MK8_Wendy_Icon:1126298934629908603>'}, 
    'Isabelle':{'Speed':3,'MiniTurbo':4.25,'Emojii':'<:MK8_Isabelle_Icon:1126298628487659570>'}, 
    'Koopa Troopa':{'Speed':3,'MiniTurbo':4.25,'Emojii':'<:MK8_Koopa_Icon:1126298677678444644>'}, 
    'Lakitu':{'Speed':3,'MiniTurbo':4.25,'Emojii':'<:MK8_Lakitu_Icon:1126298679347781662>'}, 
    'Bowser Jr.':{'Speed':3,'MiniTurbo':4.25,'Emojii':'<:MK8_Bowser_Jr_Icon:1126298582375481345>'}, 
    'Toad':{'Speed':3.25,'MiniTurbo':4.25,'Emojii':'<:MK8_Toad_Icon:1126298895518023690>'}, 
    'Shy Guy':{'Speed':3.25,'MiniTurbo':4.25,'Emojii':'<:MK8_ShyGuy_Icon:1126298893110493215>'}, 
    'Larry':{'Speed':3.25,'MiniTurbo':4.25,'Emojii':'<:MK8_Larry_Icon:1126298680840966274>'}, 
    'Cat Peach':{'Speed':3.5,'MiniTurbo':4,'Emojii':'<:MK8_Cat_Peach_Icon:1126298629418799105>'}, 
    'Inkling Girl':{'Speed':3.5,'MiniTurbo':4,'Emojii':'<:MK8DX_Female_Inkling_Icon:1126298982549815317>'}, 
    'Female Villager':{'Speed':3.5,'MiniTurbo':4,'Emojii':'<:VillagerFemaleIconMK8:1126299546759200829>'}, 
    'Peach':{'Speed':3.75,'MiniTurbo':4.25,'Emojii':'<:MK8_Peach_Icon:1126298805910908979>'}, 
    'Daisy':{'Speed':3.75,'MiniTurbo':4.25,'Emojii':'<:MK8_Daisy_Icon:1126298630802907217>'}, 
    'Yoshi':{'Speed':3.75,'MiniTurbo':4.25,'Emojii':'<:MK8_Yoshi_Icon:1126298935485534269>'}, 
    'Birdo':{'Speed':3.75,'MiniTurbo':4.25,'Emojii':'<:MK8D_Birdo_Icon:1126298976510021633>'}, 
    'Tanooki Mario':{'Speed':3.75,'MiniTurbo':4,'Emojii':'<:MK8_Tanooki_Mario_Icon:1126327270076842024>'}, 
    'Inkling Boy':{'Speed':3.75,'MiniTurbo':4,'Emojii':'<:MK8DX_Male_Inkling_Icon:1126299041282674748>'}, 
    'Male Villager':{'Speed':3.75,'MiniTurbo':4,'Emojii':'<:VillagerMaleIconMK8:1126299547677753394>'}, 
    'Mario':{'Speed':4,'MiniTurbo':4,'Emojii':'<:MK8_Mario_Icon:1126298803255922778>'}, 
    'Ludwig':{'Speed':4,'MiniTurbo':4,'Emojii':'<:MK8_Ludwig_Icon:1126298712218550272>'}, 
    'Medium Mii':{'Speed':4,'MiniTurbo':4,'Emojii':'<:Mii_MK8:1126298535449595935>'}, 
    'Luigi':{'Speed':4,'MiniTurbo':4,'Emojii':'<:MK8_Luigi_Icon:1126298707529306264>'}, 
    'Iggy':{'Speed':4,'MiniTurbo':4,'Emojii':'<:MK8_Iggy_Icon:1126298635093684264>'}, 
    'Rosalina':{'Speed':4.25,'MiniTurbo':3.75,'Emojii':'<:MK8_Rosalina_Icon:1126298801594974328>'}, 
    'King Boo':{'Speed':4.25,'MiniTurbo':3.75,'Emojii':'<:MK8DX_King_Boo_Icon:1126299037453254837>'}, 
    'Link':{'Speed':4.25,'MiniTurbo':3.75,'Emojii':'<:MK8_Link_Icon:1126298710930903050>'}, 
    'Metal Mario':{'Speed':4.25,'MiniTurbo':3.5,'Emojii':'<:MK8_MMario_Icon:1126298804136714351>'}, 
    'Gold Mario':{'Speed':4.25,'MiniTurbo':3.5,'Emojii':'<:MK8DX_Gold_Mario_Icon:1126298974962319400>'}, 
    'Pink Gold Peach':{'Speed':4.25,'MiniTurbo':3.5,'Emojii':'<:MK8_PGPeach_Icon:1126298806716219443>'}, 
    'Waluigi':{'Speed':4.5,'MiniTurbo':3.5,'Emojii':'<:MK8_Waluigi_Icon:1126298891151745074>'}, 
    'Donkey Kong':{'Speed':4.5,'MiniTurbo':3.5,'Emojii':'<:MK8_DKong_Icon:1126298631985692704>'}, 
    'Roy':{'Speed':4.5,'MiniTurbo':3.5,'Emojii':'<:MK8_Roy_Icon:1126298892082892850>'}, 
    'Wario':{'Speed':4.75,'MiniTurbo':3.25,'Emojii':'<:MK8_Wario_Icon:1126298933166088202>'}, 
    'Dry Bowser':{'Speed':4.75,'MiniTurbo':3.25,'Emojii':'<:MK8_Dry_Bowser_Icon:1126298633101393930>'}, 
    'Bowser':{'Speed':4.75,'MiniTurbo':3.25,'Emojii':'<:MK8_Bowser_Icon:1126298590332067993>'}, 
    'Morton':{'Speed':4.75,'MiniTurbo':3.25,'Emojii':'<:MK8_Morton_Icon:1126298805021704232>'}, 
    'Heavy Mii':{'Speed':4.75,'MiniTurbo':3.25,'Emojii':'<:Mii_MK8:1126298535449595935>'}
    }
KartData = {
    'Standard Kart':{'Speed':0,'MiniTurbo':0,'Emojii':'<:StandardKartBodyMK8:1126299500982571158>'}, 
    'The Duke':{'Speed':0,'MiniTurbo':0,'Emojii':'<:TheDukeBodyMK8:1126299508184190976>'}, 
    '300 SL Roadster':{'Speed':0,'MiniTurbo':0,'Emojii':'<:300SLRoadster_MK8:1126265960626655402>'}, 
    'Pipe Frame':{'Speed':-.5,'MiniTurbo':.25,'Emojii':'<:PipeFrameBodyMK8:1126299391695798392>'}, 
    'Varmint':{'Speed':-.5,'MiniTurbo':.25,'Emojii':'<:VarmintBodyMK8:1126299545354117222>'}, 
    'City Tripper':{'Speed':-.5,'MiniTurbo':.25,'Emojii':'<:MK8_LightGreen_City_Tripper:1126298709383188480>'}, 
    'Mach 8':{'Speed':0,'MiniTurbo':0,'Emojii':'<:Mach8BodyMK8:1126298532094169150>'}, 
    'Sports Coupe':{'Speed':0,'MiniTurbo':0,'Emojii':'<:SportsCoupeMK8:1126299479839092736>'}, 
    'Inkstriker':{'Speed':0,'MiniTurbo':0,'Emojii':'<:MK8DX_Inkstriker:1126299035884585122>'}, 
    'Steel Driver':{'Speed':.25,'MiniTurbo':-.5,'Emojii':'<:Steel_Driver:1126299503532720149>'}, 
    'Tri-Speeder':{'Speed':.25,'MiniTurbo':-.5,'Emojii':'<:TrispeederBodyMK8:1126299498826698773>'}, 
    'Bone Rattler':{'Speed':.25,'MiniTurbo':-.5,'Emojii':'<:MK8BoneRattler:1126298930645323777>'}, 
    'Cat Cruiser':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:CatCruiserBodyMK8:1126266037676027955>'}, 
    'Teddy Buggy':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:TeddyBuggyBodyMK8:1126299506565201921>'}, 
    'Comet':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:CometBodyMK8:1126298445519536200>'}, 
    'Yoshi Bike':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:YoshiBikeBodyMK8:1126299611829633198>'}, 
    'Circuit Special':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:CircuitSpecialBodyMK8:1126266038732984382>'}, 
    'B-Dasher':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:ZeldaMK8Bdasher:1126299544343289856>'}, 
    'P-Wing':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:MK8PWing:1126299090746085417>'}, 
    'Badwagon':{'Speed':.5,'MiniTurbo':-1,'Emojii':'<:BadwagonBodyMK8:1126265962648326334>'}, 
    'GLA':{'Speed':.5,'MiniTurbo':-1,'Emojii':'<:GLAMK8:1126298442822594632>'}, 
    'Standard ATV':{'Speed':.5,'MiniTurbo':-1,'Emojii':'<:Gold_Standard:1126298490620882984>'}, 
    'Prancer':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:PrancerBodyMK8:1126299393952338020>'}, 
    'Sport Bike':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:SportBikeBodyMK8:1126299478798905374>'}, 
    'Jet Bike':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:JetBikeBodyMK8:1126298487785525380>'},
    'Biddybuggy':{'Speed':-.75,'MiniTurbo':.5,'Emojii':'<:BiddybuggyBodyMK8:1126265963575246858>'}, 
    'Mr Scooty':{'Speed':-.75,'MiniTurbo':.5,'Emojii':'<:MrScootyBodyMK8:1126299332749045851>'}, 
    'Landship':{'Speed':-.5,'MiniTurbo':.25,'Emojii':'<:LandshipBodyMK8:1126298529648877678>'}, 
    'Streetle':{'Speed':-.5,'MiniTurbo':.25,'Emojii':'<:MK8Streetle:1126299092167954563>'}, 
    'Sneaker':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:SneakerBodyMK8:1126299476341039104>'}, 
    'Gold Standard':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:Gold_Standard:1126298490620882984>'}, 
    'Master Cycle':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:MK8D_Master_Cycle_Zero:1126298978674278461>'}, 
    'W 25 Silver Arrow':{'Speed':-.25,'MiniTurbo':0,'Emojii':'<:W25SilverArrowMK8:1126299548571148328>'}, 
    'Standard Bike':{'Speed':-.25,'MiniTurbo':0,'Emojii':'<:StandardBikeBodyMK8:1126299474512318595>'}, 
    'Flame Rider':{'Speed':-.25,'MiniTurbo':0,'Emojii':'<:FlameRiderBodyMK8:1126298441765629972>'}, 
    'Wild Wiggler':{'Speed':-.25,'MiniTurbo':0,'Emojii':'<:WildWigglerBodyMK8:1126299551742054440>'}, 
    'Blue Falcon':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:MK8BlueFalcon:1126298927763836928>'}, 
    'Splat Buggy':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:MK8DX_Splat_Buggy:1126299042704543825>'}, 
    'Tanooki Kart':{'Speed':-.25,'MiniTurbo':-.25,'Emojii':'<:MK8_Tanooki_Buggy_Sprite:1126298894494601296>'}, 
    'Koopa Clown':{'Speed':-.25,'MiniTurbo':-.25,'Emojii':'<:MK8DX_Koopa_Clown:1126299039072256030>'}, 
    'Master Cycle Zero':{'Speed':-.25,'MiniTurbo':-.25,'Emojii':'<:MK8D_Master_Cycle_Zero:1126298978674278461>'}
    }
WheelData = {
    'Standard':{'Speed':0,'MiniTurbo':0,'Emojii':'<:StandardTiresMK8:1126299502664491018>'}, 
    'Blue Standard':{'Speed':0,'MiniTurbo':0,'Emojii':'<:Blue_Standard:1126265965055856780>'}, 
    'GLA Tires':{'Speed':0,'MiniTurbo':0,'Emojii':'<:GLATiresMK8:1126298489521983618>'}, 
    'Monster':{'Speed':0,'MiniTurbo':-.25,'Emojii':'<:HotMonsterTiresMK8:1126298482819477564>'}, 
    'Hot Monster':{'Speed':0,'MiniTurbo':-.25,'Emojii':'<:HotMonsterTiresMK8:1126298482819477564>'}, 
    'Ancient Tires':{'Speed':0,'MiniTurbo':-.25,'Emojii':'<:MK8D_Ancient_Tires:1126298932004278362>'}, 
    'Roller':{'Speed':-.5,'MiniTurbo':.5,'Emojii':'<:RollerTiresMK8:1126299387044298792>'}, 
    'Azure Roller':{'Speed':-.5,'MiniTurbo':.5,'Emojii':'<:AzureRollerTiresMK8:1126265961696211014>'}, 
    'Slim':{'Speed':.25,'MiniTurbo':-.25,'Emojii':'<:SlimTiresMK8:1126299421320155167>'}, 
    'Wood':{'Speed':.25,'MiniTurbo':-.75,'Emojii':'<:WoodTiresMK8:1126299598676295822>'}, 
    'Crimson Slim':{'Speed':.25,'MiniTurbo':-.75,'Emojii':'<:CrimsonSlimTiresMK8:1126266033804673044>'}, 
    'Slick':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:SlickTiresMK8:1126299421999644733>'}, 
    'Cyber Slick':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:CyberSlickTiresMK8:1126298448946278472>'}, 
    'Metal':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:MetalTiresMK8:1126298533927071856>'}, 
    'Gold Tires':{'Speed':.5,'MiniTurbo':-.75,'Emojii':'<:Gold_Tires_MK8:1126298491728171068>'}, 
    'Button':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:ButtonTiresMK8:1126266036002508820>'}, 
    'Leaf Tires':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:Leaf_Tires_MK8:1126298531062370445>'}, 
    'Off-Road':{'Speed':.25,'MiniTurbo':-.5,'Emojii':'<:OffRoad:1126299333583716403>'}, 
    'Retro Off-Road':{'Speed':.25,'MiniTurbo':-.5,'Emojii':'<:Retro_OffRoad:1126299394950561902>'}, 
    'Triforce Tires':{'Speed':.25,'MiniTurbo':-.5,'Emojii':'<:MK8TriforceTires:1126299093153624125>'}, 
    'Sponge':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:SpongeTiresMK8:1126299477213466685>'}, 
    'Cushion':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:CushionTiresMK8:1126298448061276182>'}
    }
GliderData = {
    'Super Glider':{'Speed':0,'MiniTurbo':0,'Emojii':'<:SuperGliderMK8:1126299505277546657>'}, 
    'Waddle Wing':{'Speed':0,'MiniTurbo':0,'Emojii':'<:WaddleWingMK8:1126299549594554421>'}, 
    'Hylian Kite':{'Speed':0,'MiniTurbo':0,'Emojii':'<:MK8HylianKite:1126299034932478032>'}, 
    'Cloud Glider':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:Cloud_Glider:1126266040893054996>'}, 
    'Parachute':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:ParachuteGliderMK8:1126299330274414623>'}, 
    'Flower Glider':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:FlowerGliderMK8:1126342650799341608>'}, 
    'Paper Glider':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:PaperGliderIconMK8:1126299328634437675>'}, 
    'Wario Wing':{'Speed':0,'MiniTurbo':0,'Emojii':'<:WarioWingMK8:1126299550748004382>'}, 
    'Plane Glider':{'Speed':0,'MiniTurbo':0,'Emojii':'<:PlaneGliderMK8:1126299393067339796>'}, 
    'Gold Glider':{'Speed':0,'MiniTurbo':0,'Emojii':'<:GoldGliderMK8:1126298492692873277>'}, 
    'Paraglider':{'Speed':0,'MiniTurbo':0,'Emojii':'<:MK8D_Paraglider:1126298979831914538>'}, 
    'Peach Parasol':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:PeachParasolGliderMK8:1126299390567514183>'}, 
    'Parafoil':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:ParafoilGliderMK8:1126299389225341041>'}, 
    'Bowser Kite':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:BowserKiteMK8:1126265958173003828>'}, 
    'MKTV Parafoil':{'Speed':-.25,'MiniTurbo':.25,'Emojii':'<:MKTVParafoilGliderMK8:1126299094663577690>'}
    }
