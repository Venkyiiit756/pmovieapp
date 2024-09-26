from flask import Flask, render_template, request, jsonify
import os
import requests
import json
import datetime
import pandas as pd

app = Flask(__name__)

# List of cities (full list as provided by the user)
cities = ['hyderabad', 'chennai']
"""cities = [
    'ahmedabad', 'ambala', 'amritsar', 'bengaluru', 'bathinda', 'bhopal', 'chandigarh',
    'coimbatore', 'delhi-ncr', 'gwalior', 'hubli', 'hyderabad', 'jaipur', 'kochi',
    'kolkata', 'kota', 'lucknow', 'ludhiana', 'mangalore', 'mumbai', 'panipat',
    'patna', 'pune', 'surat', 'thane', 'vadodara', 'vijayawada', 'bharuch', 'anand',
    'panchkula', 'dhanbad', 'aurangabad', 'nashik', 'chennai', 'vizianagaram',
    'navi-mumbai', 'nagpur', 'indore', 'goa', 'raipur', 'durgapur', 'faridabad',
    'burdwan', 'vizag', 'kanpur', 'belagavi', 'siliguri', 'bhubaneswar', 'udaipur',
    'kalyan', 'madurai', 'greater-noida', 'jalgaon', 'manipal', 'gurgaon',
    'new-delhi', 'jodhpur', 'mysuru', 'kurnool', 'bhilwara', 'ajmer', 'gandhinagar',
    'rajkot', 'bhiwadi', 'thrissur', 'jorhat', 'meerut', 'allahabad', 'balaghat',
    'bhilai', 'bilaspur', 'bokaro', 'dehradun', 'gandhidham', 'guwahati',
    'haridwar', 'jalandhar', 'jammu', 'kalaburagi', 'kolhapur', 'latur', 'mohali',
    'moradabad', 'nanded', 'neemuch', 'pathankot', 'rudrapur', 'sikar', 'ujjain',
    'bhimavaram', 'alappuzha', 'trichy', 'amalapuram', 'saharanpur', 'anakapalle',
    'attili', 'kozhikode', 'chilakaluripet', 'chirala', 'draksharamam', 'eluru',
    'guntakal', 'guntur', 'gurazala', 'kakinada', 'kasibugga', 'macherla',
    'machilipatnam', 'mandapeta', 'mylavaram', 'nandyal', 'narasaraopet',
    'narsapur', 'narsipatnam', 'nellore', 'nuziveedu', 'palasa', 'parvathipuram',
    'payakaraopeta', 'peddapuram', 'rajahmundry', 'ramachandrapuram',
    'ravulapalem', 'samalkota', 'sattenapalle', 'srikakulam', 'tadepalligudem',
    'tekkali', 'tenali', 'tiruvuru', 'vinukonda', 'vissannapeta', 'rewari',
    'vijayapura', 'gadag', 'kalpetta', 'kottarakara', 'malappuram', 'mananthavady',
    'manjeri', 'mukkam', 'payyanur', 'perinthalmanna', 'ponnani', 'punalur',
    'tirur', 'satna', 'puducherry', 'dharapuram', 'erode', 'hosur', 'karimangalam',
    'katpadi', 'komarapalayam', 'pollachi', 'rajapalayam', 'sivakasi', 'thanjavur',
    'theni', 'tirunelveli', 'tirupur', 'bhuvanagiri', 'dubbak', 'godavarikhani',
    'kalwakurthy', 'karimnagar', 'khammam', 'madhira', 'mancherial', 'metpally',
    'miryalaguda', 'nalgonda', 'nizamabad', 'parigi', 'sangareddi', 'sathupally',
    'secunderabad', 'shadnagar', 'suryapet', 'tandur', 'warangal', 'bareilly',
    'gorakhpur', 'jhansi', 'muzaffarnagar', 'kanhangad', 'avinashi', 'tirupati',
    'pennagaram', 'kavali', 'alwar', 'dausa', 'mathura', 'shri-ganganagar',
    'salem', 'junagadh', 'jagdalpur', 'jetpur', 'ankleshwar', 'balasore',
    'rewa', 'ahmednagar', 'chandrapur', 'betul', 'guna', 'sarni', 'karnal',
    'asansol', 'agra', 'aligarh', 'jamshedpur', 'andul', 'howrah', 'athagarh',
    'roorkee', 'ropar', 'dhamtari', 'doraha', 'ghaziabad', 'ghazipur',
    'himmatnagar', 'jalpaiguri', 'kaithal', 'noida', 'loni', 'kothapeta',
    'narasannapeta', 'vuyyuru', 'vapi', 'krishnagiri', 'armoor', 'bhupalapalli',
    'valsad', 'gondia', 'nadiad', 'kanchipuram', 'adipur', 'kawardha',
    'kondagaon', 'indapur', 'rahuri', 'gajapathinagaram', 'palluruthy',
    'akola', 'amravati', 'angamaly', 'bikaner', 'chhindwara', 'dindigul',
    'durg', 'rajnandgaon', 'halol', 'jamnagar', 'khandwa', 'kishangarh',
    'kollam', 'kurukshetra', 'muzaffarpur', 'malout', 'patan', 'ranchi',
    'sangli', 'sonipat', 'ulhasnagar', 'vasai', 'yamunanagar', 'zirakpur',
    'kotkapura', 'moga', 'yavatmal', 'dabhoi', 'dahod', 'baloda-bazar',
    'etawah', 'haldwani', 'barwani', 'bulandshahr', 'hisar', 'kashipur',
    'bhuj', 'bellary', 'dhuri', 'kalol', 'tinsukia', 'raigarh', 'bhavnagar',
    'hathras', 'surendranagar', 'palghar', 'ichalkaranji', 'abohar',
    'khambhat', 'baddi', 'edappal', 'cuddalore', 'hoshiarpur', 'dasuya',
    'muvattupuzha', 'udgir', 'tadipatri', 'mudhol', 'ashtamichira',
    'saligram', 'pattambi', 'khanapur', 'yellandu', 'chidambaram',
    'chhatarpur', 'varanasi', 'mughalsarai', 'tirumalgiri', 'deesa', 'idar',
    'nagaon', 'sanand', 'kichha', 'raebareli', 'navsari', 'mehsana',
    'bayad', 'siddhpur', 'shillong', 'kodaly', 'podili', 'tuticorin',
    'palakonda', 'thiruvarur', 'darsi', 'kozhinjampara', 'gudivada',
    'ranebennur', 'cumbum', 'palakkad', 'chamarajanagara', 'nagercoil',
    'varadium', 'gorantla', 'ulundurpet', 'vijapur', 'wani', 'kullu',
    'bahadurgarh', 'digras', 'dhule', 'rourkela', 'pithampur',
    'ashoknagar', 'mansa', 'kekri', 'cuttack', 'davanagere', 'shivpuri',
    'gadarwara', 'bhusawal', 'kopargaon', 'kalol-panchmahal', 'pendra',
    'dalli-rajhara', 'mangaldoi', 'sivasagar', 'firozepur', 'kodungallur',
    'hanumangarh', 'karad', 'dewas', 'gaya', 'dimapur', 'itarsi',
    'beawar', 'adoni', 'unnao', 'kareli', 'dharwad', 'chitradurga',
    'jind', 'bagalkot', 'ratlam', 'sagwara', 'shivamogga', 'khanna',
    'ambikapur', 'bhandara', 'faizabad', 'kundli', 'nimbahera',
    'arambagh', 'aurangabad-west-bengal', 'krishnanagar', 'dubrajpur',
    'thalassery', 'dhampur', 'khopoli', 'pandharpur', 'sitapur', 'dharamsala',
    'sundargarh', 'jamkhed', 'addanki', 'ponnur', 'atmakur', 'anjar',
    'bobbili', 'jhabua', 'nawanshahr', 'pithapuram', 'tatipaka',
    'pipariya', 'seoni-malwa', 'hamirpur', 'korba', 'anantapur',
    'gurdaspur', 'tumkur', 'banga', 'morena', 'azamgarh',
    'pratapgarh-uttar-pradesh', 'dibrugarh', 'palampur', 'nawapara',
    'fazilka', 'jangaon', 'rajam', 'jirapur', 'pilkhuwa', 'jalalabad',
    'dehgam', 'bhadravati', 'port-blair', 'aruppukkottai', 'sivagangai',
    'devakottai', 'nandurbar', 'palani', 'mannarkkad', 'repalle',
    'berhampur', 'jiaganj', 'khargone', 'trivandrum', 'kanchikacherla',
    'hanuman-junction', 'kaikaluru', 'naidupeta', 'atmakur-nellore',
    'madanapalle', 'punganur', 'kuppam', 'jaggampeta', 'yeleswaram',
    'hajipur', 'burhanpur', 'jajpur-road', 'kalimpong', 'bapatla',
    'mukhed', 'motihari', 'tuni', 'baghapurana', 'lonavala', 'tanda',
    'hindaun', 'singarayakonda', 'venkatagiri', 'dongargarh',
    'bakhrahat', 'sultanpur', 'madugula', 'rupnagar', 'morinda',
    'junnar', 'gopalganj', 'kolar', 'malikipuram', 'cooch-behar',
    'shirpur', 'rayagada', 'mahabubabad', 'angul', 'mundra',
    'nandigama', 'neelapalle', 'petlad', 'uthukottai', 'amreli',
    'kunnamkulam', 'cheepurupalli', 'chittoor', 'dharmavaram',
    'ganapavaram', 'kandukur', 'markapuram', 'mogalthur', 'nagari',
    'nindra', 'proddatur', 'saluru', 'yemmiganur', 'adoor',
    'amballur', 'chalakudy', 'guruvayur', 'irinjalakuda',
    'kattanam', 'kodakara', 'koothattukulam', 'peringottukara',
    'thalikulam', 'thiruvalla', 'valanchery', 'wadakkancherry',
    'acharapakkam', 'ambur', 'ammaiyarkuppam', 'annur', 'anthiyur',
    'arakkonam', 'batlagundu', 'eriyur', 'kallakurichi', 'kangeyam',
    'karaikudi', 'kulithalai', 'kumbakonam', 'muthur', 'namakkal',
    'perundalaiyur', 'perundurai', 'pudukkottai', 'ramanathapuram',
    'sankarankovil', 'sathankulam', 'sethiyathope', 'somanur',
    'tenkasi', 'thiruthani', 'thiruvannamalai', 'thuraiyur',
    'tiruchendur', 'tirukoilur', 'udumalpet', 'vedaranyam',
    'vellakoil', 'vellore', 'bonakal', 'chevella', 'nirmal',
    'krosuru', 'cherukupalli', 'railway-koduru', 'godhra',
    'dholka', 'tohana', 'giridih', 'bodi', 'villupuram',
    'islampur', 'singrauli', 'sangrur', 'kotdwar', 'dharmaj',
    'kapadvanj', 'fatehabad', 'punjai-puliampatti',
    'north-paravur', 'kuchaman', 'kavindapadi', 'alangayam',
    'agartala', 'mullanpur', 'palakollu', 'kadiri', 'kovvur',
    'kadapa', 'chagallu', 'duggirala', 'allagadda', 'kotabommali',
    'gudur-kurnool', 'palamaner', 'nallamada', 'kothacheruvu',
    'nidadavolu', 'bestavaripeta', 'chebrolu', 'nellimarla',
    'nallajerla', 'hiramandalam', 'palvancha', 'himatnagar',
    'domkal', 'sultan-bathery', 'penuganchiprolu', 'pamur',
    'rayachoti', 'tanguturu', 'uppada', 'pathapatnam',
    'pedana', 'somandepalle', 'pamidi', 'shahpur',
    'dandeli', 'sidlaghatta', 'udupi', 'koratagere', 'sirsi',
    'chikkaballapura', 'tiptur', 'pavagada', 'ankola',
    'kambainallur', 'tiruchengode', 'thammampatti', 'rasipuram',
    'jalakandapuram', 'valapadi', 'tirupattur', 'kaveripattinam',
    'mettur', 'chinnasalem', 'sankagiri', 'pallipalayam',
    'bommidi', 'jammikunta', 'parkal', 'thorrur', 'chityal',
    'kamanpur', 'choutuppal', 'huzurabad', 'huzurnagar',
    'kothagudem', 'sirpur-kagaznagar', 'valigonda', 'ieeja',
    'ambernath', 'akividu', 'bilgi', 'kodumur', 'panruti',
    'rabkavi', 'daryapur', 'dhone', 'jami', 'ponduru',
    'ichchapuram', 'satyavedu', 'gokavaram', 'deoghar',
    'sindagi', 'katni', 'vijayamangalam', 'gingee',
    'gobichettipalayam', 'idappadi', 'ambasamudram',
    'kadayam', 'bellampally', 'mukerian', 'dinanagar',
    'jayamkondan', 'banswada', 'kota-nellore', 'peravurani',
    'mudalgi', 'sankeshwar', 'umbergaon', 'pandikkad',
    'neyveli', 'jamkhambhaliya', 'katihar', 'bijainagar',
    'kovilpatti', 'harur', 'sakti', 'hapur', 'nadia',
    'sambalpur', 'jharsuguda', 'gauribidanur', 'sujangarh',
    'puliyankudi', 'kurinjipadi', 'hardoi', 'silchar',
    'mattanur', 'kotpad', 'thanipadi', 'uthangarai',
    'patiala', 'pedakurapadu', 'chinnamanur', 'titagarh',
    'patran', 'sirsa', 'batala', 'khamgaon',
    'lakhimpur-uttar-pradesh', 'srikalahasti', 'sardulgarh',
    'nagapattinam', 'mala', 'bhagalpur', 'washim',
    'berachampa', 'changaramkulam', 'sambhal', 'jeypore',
    'dabra', 'ponnamaravathi', 'thiruthuraipoondi',
    'nambiyur', 'jamtara', 'narwana', 'sugauli',
    'mandi-gobindgarh', 'paralakhemundi', 'arumbavur',
    'sullurpeta', 'sirkali', 'koratla', 'bagepalli',
    'kuzhithurai', 'banaganapalli', 'bagnan', 'jaunpur',
    'mayiladuthurai', 'palacode', 'forbesganj', 'kotputli',
    'pusad', 'morbi', 'narnaul', 'jejuri', 'khurja',
    'raxaul', 'alangudi', 'ekma-chapra', 'bundu', 'barhi',
    'alakode', 'dharmapuri', 'tezpur', 'silvassa',
    'surandai', 'cherpulassery', 'golaghat', 'bijapur',
    'veraval', 'kalyani', 'kalakad', 'karur', 'chiplun',
    'paramathivelur', 'saharsa', 'purnia', 'keeranur',
    'samastipur', 'dumka', 'lakhimpur-assam', 'nabadwip',
    'kokrajhar', 'ramabhadrapuram', 'dhanera', 'attur',
    'bhadohi', 'chanpatia', 'malda', 'raiganj',
    'sumerpur', 'borsad', 'daman', 'karwar',
    'nelakondapally', 'mandvi', 'khandela',
    'sathyamangalam', 'periyakulam', 'bazpur',
    'damoh', 'krishnarajanagara', 'siruvalur',
    'talwandi-bhai', 'pileru', 'falna',
    'pulivendula', 'ron', 'chotila', 'gundlupet',
    'chennur', 'una', 'luxettipet', 'hoogly',
    'supaul', 'hazaribagh', 'Nathdwara', 'tittagudi',
    'Valliyur', 'Viralimalai', 'Balanagar',
    'Koottanad', 'Pirangut', 'Shirur', 'marthandam',
    'cherupuzha', 'budaun', 'undavalli', 'mau',
    'akbarpur', 'kankipadu', 'kakkattil', 'arni',
    'srivilliputhur', 'kollengode', 'velanthavalam',
    'sindhanur', 'kheda', 'mummidivaram', 'aranthangi',
    'nazirpur', 'gohana', 'raichur', 'jabalpur',
    'nava-raipur', 'jagraon', 'cheruvathur',
    'bharatpur', 'palasa-kasibugga', 'malkipuram',
    'p-dharmavaram', 'chimakurthy', 'maduranthakam',
    'sunam', 'waterland', 'budhlada', 'kottakkal',
    'wandoor', 'kolathur', 'farrukhabad', 'nichlaul',
    'vrindavan', 'edacheri', 'kangra', 'mandi',
    'chamba', 'sirmaur', 'kinnaur', 'razole',
    'nakrekal', 'firozabad', 'kurumassery',
    'kondotty', 'vita', 'tumakuru', 'tindivanam',
    'neyveli-township', 'bilaspur-himachal-pradesh',
    'virudhachalam', 'nanjangud', 'bibinagar',
    'bhongir', 'thavanampalle', 'umreth',
    'bangarupallem', 'anaikatti', 'balasinor',
    'chintamani', 'pali', 'kanipakam', 'nagireddypet',
    'jalore', 'yelamanchili', 'elamanchili',
    'panachamoodu', 'west-champaran', 'gudur-nellore',
    'sathupalli', 'thiruppathur', 'kolargoldfields',
    'hoshangabad', 'andimadam', 'gopiganj', 'ariyalur',
    'parawada', 'basantpur', 'chandausi', 'ottapalam',
    'falakata', 'kanigiri', 'mappedu', 'srinagar',
    'nagaram', 'amangal', 'velangi', 'gudiyatham',
    'cheyyar', 'arcot', 'ranipet', 'vaniyambadi',
    'sonari', 'kondur', 'perambra', 'puttur',
    'jhunjhunu', 'lalgudi', 'manapparai',
    'krishnarajpet', 'malur', 'ranastalam',
    'kothampakkam', 'rajampet', 'vyara',
    'ghumarwin', 'melli', 'una-gujarat', 'kotma',
    'mahalingpur', 'gauriganj', 'melattur',
    'vandavasi', 'burhar', 'chaygaon',
    'sankarapuram', 'sholinghur', 'halduchour',
    'lalkuan', 'pantnagar', 'thiruvallur',
    'marpally', 'kolappalur', 'gondal', 'bhainsa',
    'kankroli', 'koheda', 'gadwal', 'haveri',
    'pernambut', 'mettupalayam', 'sukma',
    'dantewada', 'koilkuntla', 'ayodhya',
    'marandahalli', 'karanja-lad', 'paonta-sahib',
    'eral', 'authoor', 'putturap', 'gajuwaka',
    'newtehri', 'kunnamangalam', 'ramgarh',
    'hindupuram', 'vettaikaranpudur', 'kolumam',
    'thiruvalangadu', 'koderma', 'devgad',
    'handwara', 'baramulla', 'atraulia',
    'kayamkulam', 'sathuvachari', 'sahjanwa',
    'greater-mumbai', 'karanodai', 'palladam',
    'penumuru', 'rath', 'pallipattu', 'pulgaon',
    'curchorem', 'choondal', 'kalady',
    'bengaluru', 'chennai', 'coimbatore',
    'delhi-ncr', 'hyderabad', 'kolkata', 'madurai',
    'puducherry', 'tirupur', 'trivandrum', 'vijayawada', 'vizag'
]"""

# Base API URL (replace 'hyderabad' with the actual city name in the loop)
base_url = "https://apiproxy.paytm.com/v3/movies/search/movie?meta=1&reqData=1&city={}&movieCode=ttdx_wuyn&version=3&site_id=6&channel=HTML5&child_site_id=370&client_id=ticketnew&clientId=ticketnew"

# Directory to save JSON files
json_directory = "cityJsons"

# Ensure the JSON directory exists
if not os.path.exists(json_directory):
    os.makedirs(json_directory)

def fetch_city_data(city):
    """Fetch data for a specific city and save as JSON."""
    api_url = base_url.format(city)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            json_data = response.json()
            with open(os.path.join(json_directory, f"{city}.json"), 'w') as json_file:
                json.dump(json_data, json_file, indent=4)
            print(f"Fetched and saved data for {city}")
            return json_data
        else:
            print(f"Failed to fetch data for {city}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return None

def load_all_data(selected_cities):
    """Load JSON data for selected cities, fetching from API if not cached."""
    data = {}
    for city in selected_cities:
        file_path = os.path.join(json_directory, f"{city}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data[city] = json.load(file)
            print(f"Loaded cached data for {city}")
        else:
            fetched_data = fetch_city_data(city)
            if fetched_data:
                data[city] = fetched_data
    return data

def process_data(data):
    """Process JSON data into structured format."""
    processed = {
        "CityData": [],
        "TheaterData": [],
        "ShowData": [],
        "CategoryData": []
    }

    for city, city_info in data.items():
        for cinema in city_info.get("meta", {}).get("cinemas", []):
            theater_name = cinema.get("name", "N/A")
            cinema_id = str(cinema.get("id", "N/A"))
            sessions = city_info.get("pageData", {}).get("sessions", {}).get(cinema_id, [])

            for session in sessions:
                audi = session.get("audi", "N/A")
                show_time = session.get("showTime", "N/A")
                key = (theater_name, audi, show_time)

                for area in session.get("areas", []):
                    label = area.get("label", "N/A")
                    sAvailTickets = area.get("sAvail", 0)
                    sTotalTickets = area.get("sTotal", 0)
                    price = area.get("price", 0)
                    sBookedTickets = sTotalTickets - sAvailTickets

                    sTotalGross = sTotalTickets * price
                    sBookedGross = sBookedTickets * price

                    # Append to ShowData
                    processed["ShowData"].append({
                        "City": city,
                        "Theater": theater_name,
                        "Audi": audi,
                        "ShowTime": show_time,
                        "Category": label,
                        "AvailableTickets": sAvailTickets,
                        "TotalTickets": sTotalTickets,
                        "BookedTickets": sBookedTickets,
                        "TotalGross": sTotalGross,
                        "BookedGross": sBookedGross
                    })

                    # Accumulate data for TheaterData
                    processed["TheaterData"].append({
                        "City": city,
                        "Theater": theater_name,
                        "Audi": audi,
                        "ShowTime": show_time,
                        "AvailableTickets": sAvailTickets,
                        "TotalTickets": sTotalTickets,
                        "BookedTickets": sBookedTickets,
                        "TotalGross": sTotalGross,
                        "BookedGross": sBookedGross
                    })

        # Aggregate for CityData
        theater_df = pd.DataFrame(processed["TheaterData"])
        city_summary = theater_df.groupby("City").agg({
            "AvailableTickets": "sum",
            "TotalTickets": "sum",
            "BookedTickets": "sum",
            "TotalGross": "sum",
            "BookedGross": "sum"
        }).reset_index()

        for _, row in city_summary.iterrows():
            processed["CityData"].append(row.to_dict())

    # Aggregate for CategoryData
    show_df = pd.DataFrame(processed["ShowData"])
    category_summary = show_df.groupby(["City", "Category"]).agg({
        "AvailableTickets": "sum",
        "TotalTickets": "sum",
        "BookedTickets": "sum",
        "TotalGross": "sum",
        "BookedGross": "sum"
    }).reset_index()

    for _, row in category_summary.iterrows():
        processed["CategoryData"].append(row.to_dict())

    return processed

@app.route('/')
def index():
    return render_template('index.html', cities=cities)

@app.route('/get_data', methods=['POST'])
def get_data():
    selected_cities = request.json.get('cities', [])
    if not selected_cities:
        return jsonify({"error": "No cities selected."}), 400

    # Handle "all" selection
    if "all" in selected_cities:
        selected_cities = cities

    data = load_all_data(selected_cities)
    if not data:
        return jsonify({"error": "No data found for the selected cities."}), 404

    processed = process_data(data)

    return jsonify(processed)

if __name__ == '__main__':
    app.run(debug=True)