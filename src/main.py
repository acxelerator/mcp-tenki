from domain.weather import WeatherForecast
from domain.location import Location

import httpx
from typing import Any

from mcp.server.fastmcp import FastMCP

USER_AGENT = "cmp-tenki-app/1.0"
# Initialize FastMCP server
mcp = FastMCP("weather")
location_data = [
    {"pref": "北海道", "city": "稚内", "id": "011000"},
    {"pref": "北海道", "city": "旭川", "id": "012010"},
    {"pref": "北海道", "city": "留萌", "id": "012020"},
    {"pref": "北海道", "city": "網走", "id": "013010"},
    {"pref": "北海道", "city": "北見", "id": "013020"},
    {"pref": "北海道", "city": "紋別", "id": "013030"},
    {"pref": "北海道", "city": "根室", "id": "014010"},
    {"pref": "北海道", "city": "釧路", "id": "014020"},
    {"pref": "北海道", "city": "帯広", "id": "014030"},
    {"pref": "北海道", "city": "室蘭", "id": "015010"},
    {"pref": "北海道", "city": "浦河", "id": "015020"},
    {"pref": "北海道", "city": "札幌", "id": "016010"},
    {"pref": "北海道", "city": "岩見沢", "id": "016020"},
    {"pref": "北海道", "city": "倶知安", "id": "016030"},
    {"pref": "北海道", "city": "函館", "id": "017010"},
    {"pref": "北海道", "city": "江差", "id": "017020"},
    {"pref": "青森県", "city": "青森", "id": "020010"},
    {"pref": "青森県", "city": "むつ", "id": "020020"},
    {"pref": "青森県", "city": "八戸", "id": "020030"},
    {"pref": "岩手県", "city": "盛岡", "id": "030010"},
    {"pref": "岩手県", "city": "宮古", "id": "030020"},
    {"pref": "岩手県", "city": "大船渡", "id": "030030"},
    {"pref": "宮城県", "city": "仙台", "id": "040010"},
    {"pref": "宮城県", "city": "白石", "id": "040020"},
    {"pref": "秋田県", "city": "秋田", "id": "050010"},
    {"pref": "秋田県", "city": "横手", "id": "050020"},
    {"pref": "山形県", "city": "山形", "id": "060010"},
    {"pref": "山形県", "city": "米沢", "id": "060020"},
    {"pref": "山形県", "city": "酒田", "id": "060030"},
    {"pref": "山形県", "city": "新庄", "id": "060040"},
    {"pref": "福島県", "city": "福島", "id": "070010"},
    {"pref": "福島県", "city": "小名浜", "id": "070020"},
    {"pref": "福島県", "city": "若松", "id": "070030"},
    {"pref": "茨城県", "city": "水戸", "id": "080010"},
    {"pref": "茨城県", "city": "土浦", "id": "080020"},
    {"pref": "栃木県", "city": "宇都宮", "id": "090010"},
    {"pref": "栃木県", "city": "大田原", "id": "090020"},
    {"pref": "群馬県", "city": "前橋", "id": "100010"},
    {"pref": "群馬県", "city": "みなかみ", "id": "100020"},
    {"pref": "埼玉県", "city": "さいたま", "id": "110010"},
    {"pref": "埼玉県", "city": "熊谷", "id": "110020"},
    {"pref": "埼玉県", "city": "秩父", "id": "110030"},
    {"pref": "千葉県", "city": "千葉", "id": "120010"},
    {"pref": "千葉県", "city": "銚子", "id": "120020"},
    {"pref": "千葉県", "city": "館山", "id": "120030"},
    {"pref": "東京都", "city": "東京", "id": "130010"},
    {"pref": "東京都", "city": "大島", "id": "130020"},
    {"pref": "東京都", "city": "八丈島", "id": "130030"},
    {"pref": "東京都", "city": "父島", "id": "130040"},
    {"pref": "神奈川県", "city": "横浜", "id": "140010"},
    {"pref": "神奈川県", "city": "小田原", "id": "140020"},
    {"pref": "新潟県", "city": "新潟", "id": "150010"},
    {"pref": "新潟県", "city": "長岡", "id": "150020"},
    {"pref": "新潟県", "city": "高田", "id": "150030"},
    {"pref": "新潟県", "city": "相川", "id": "150040"},
    {"pref": "富山県", "city": "富山", "id": "160010"},
    {"pref": "富山県", "city": "伏木", "id": "160020"},
    {"pref": "石川県", "city": "金沢", "id": "170010"},
    {"pref": "石川県", "city": "輪島", "id": "170020"},
    {"pref": "福井県", "city": "福井", "id": "180010"},
    {"pref": "福井県", "city": "敦賀", "id": "180020"},
    {"pref": "山梨県", "city": "甲府", "id": "190010"},
    {"pref": "山梨県", "city": "河口湖", "id": "190020"},
    {"pref": "長野県", "city": "長野", "id": "200010"},
    {"pref": "長野県", "city": "松本", "id": "200020"},
    {"pref": "長野県", "city": "飯田", "id": "200030"},
    {"pref": "岐阜県", "city": "岐阜", "id": "210010"},
    {"pref": "岐阜県", "city": "高山", "id": "210020"},
    {"pref": "静岡県", "city": "静岡", "id": "220010"},
    {"pref": "静岡県", "city": "網代", "id": "220020"},
    {"pref": "静岡県", "city": "三島", "id": "220030"},
    {"pref": "静岡県", "city": "浜松", "id": "220040"},
    {"pref": "愛知県", "city": "名古屋", "id": "230010"},
    {"pref": "愛知県", "city": "豊橋", "id": "230020"},
    {"pref": "三重県", "city": "津", "id": "240010"},
    {"pref": "三重県", "city": "尾鷲", "id": "240020"},
    {"pref": "滋賀県", "city": "大津", "id": "250010"},
    {"pref": "滋賀県", "city": "彦根", "id": "250020"},
    {"pref": "京都府", "city": "京都", "id": "260010"},
    {"pref": "京都府", "city": "舞鶴", "id": "260020"},
    {"pref": "大阪府", "city": "大阪", "id": "270000"},
    {"pref": "兵庫県", "city": "神戸", "id": "280010"},
    {"pref": "兵庫県", "city": "豊岡", "id": "280020"},
    {"pref": "奈良県", "city": "奈良", "id": "290010"},
    {"pref": "奈良県", "city": "風屋", "id": "290020"},
    {"pref": "和歌山県", "city": "和歌山", "id": "300010"},
    {"pref": "和歌山県", "city": "潮岬", "id": "300020"},
    {"pref": "鳥取県", "city": "鳥取", "id": "310010"},
    {"pref": "鳥取県", "city": "米子", "id": "310020"},
    {"pref": "島根県", "city": "松江", "id": "320010"},
    {"pref": "島根県", "city": "浜田", "id": "320020"},
    {"pref": "島根県", "city": "西郷", "id": "320030"},
    {"pref": "岡山県", "city": "岡山", "id": "330010"},
    {"pref": "岡山県", "city": "津山", "id": "330020"},
    {"pref": "広島県", "city": "広島", "id": "340010"},
    {"pref": "広島県", "city": "庄原", "id": "340020"},
    {"pref": "山口県", "city": "下関", "id": "350010"},
    {"pref": "山口県", "city": "山口", "id": "350020"},
    {"pref": "山口県", "city": "柳井", "id": "350030"},
    {"pref": "山口県", "city": "萩", "id": "350040"},
    {"pref": "徳島県", "city": "徳島", "id": "360010"},
    {"pref": "徳島県", "city": "日和佐", "id": "360020"},
    {"pref": "香川県", "city": "高松", "id": "370000"},
    {"pref": "愛媛県", "city": "松山", "id": "380010"},
    {"pref": "愛媛県", "city": "新居浜", "id": "380020"},
    {"pref": "愛媛県", "city": "宇和島", "id": "380030"},
    {"pref": "高知県", "city": "高知", "id": "390010"},
    {"pref": "高知県", "city": "室戸岬", "id": "390020"},
    {"pref": "高知県", "city": "清水", "id": "390030"},
    {"pref": "福岡県", "city": "福岡", "id": "400010"},
    {"pref": "福岡県", "city": "八幡", "id": "400020"},
    {"pref": "福岡県", "city": "飯塚", "id": "400030"},
    {"pref": "福岡県", "city": "久留米", "id": "400040"},
    {"pref": "佐賀県", "city": "佐賀", "id": "410010"},
    {"pref": "佐賀県", "city": "伊万里", "id": "410020"},
    {"pref": "長崎県", "city": "長崎", "id": "420010"},
    {"pref": "長崎県", "city": "佐世保", "id": "420020"},
    {"pref": "長崎県", "city": "厳原", "id": "420030"},
    {"pref": "長崎県", "city": "福江", "id": "420040"},
    {"pref": "熊本県", "city": "熊本", "id": "430010"},
    {"pref": "熊本県", "city": "阿蘇乙姫", "id": "430020"},
    {"pref": "熊本県", "city": "牛深", "id": "430030"},
    {"pref": "熊本県", "city": "人吉", "id": "430040"},
    {"pref": "大分県", "city": "大分", "id": "440010"},
    {"pref": "大分県", "city": "中津", "id": "440020"},
    {"pref": "大分県", "city": "日田", "id": "440030"},
    {"pref": "大分県", "city": "佐伯", "id": "440040"},
    {"pref": "宮崎県", "city": "宮崎", "id": "450010"},
    {"pref": "宮崎県", "city": "延岡", "id": "450020"},
    {"pref": "宮崎県", "city": "都城", "id": "450030"},
    {"pref": "宮崎県", "city": "高千穂", "id": "450040"},
    {"pref": "鹿児島県", "city": "鹿児島", "id": "460010"},
    {"pref": "鹿児島県", "city": "鹿屋", "id": "460020"},
    {"pref": "鹿児島県", "city": "種子島", "id": "460030"},
    {"pref": "鹿児島県", "city": "名瀬", "id": "460040"},
    {"pref": "沖縄県", "city": "那覇", "id": "471010"},
    {"pref": "沖縄県", "city": "名護", "id": "471020"},
    {"pref": "沖縄県", "city": "久米島", "id": "471030"},
    {"pref": "沖縄県", "city": "南大東", "id": "472000"},
    {"pref": "沖縄県", "city": "宮古島", "id": "473000"},
    {"pref": "沖縄県", "city": "石垣島", "id": "474010"},
    {"pref": "沖縄県", "city": "与那国島", "id": "474020"},
]


async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


def convert_pref_to_id(prefecture: str) -> Location | None:
    locations = [Location(**d) for d in location_data]
    location_in_prefecture = [l for l in locations if l.prefecture == prefecture]
    if len(location_in_prefecture) == 0:
        return None
    else:
        return location_in_prefecture[0]


@mcp.tool()
async def get_forecast(prefecture: str) -> str:
    """
    Get forecast for a location in Japan

    Args:
        prefecture: Name of the prefecture of Japan
    """
    id_ = convert_pref_to_id(prefecture=prefecture)
    url = f"https://weather.tsukumijima.net/api/forecast?city={id_}"
    res = await make_nws_request(url=url)

    if not res:
        return "Unable to fetch forecast data for this location."
    forecasts = [WeatherForecast(**f) for f in res["forecasts"]]
    return "\n------\n".join([f.format_forecast() for f in forecasts])

