import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_groq import ChatGroq
from langchain.chains import GraphCypherQAChain


load_dotenv()

graph=Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)


llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama3-8b-8192")


users_query = """
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/vansh-khaneja/test5/main/amazon_prime_users.csv' AS row

MERGE (person:Person {name: COALESCE(row.`Name`, 'Unknown'), email: COALESCE(row.`Email Address`, 'Unknown Email')})
MERGE (location:Location {name: COALESCE(row.`Location`, 'Unknown Location')})
MERGE (plan:SubscriptionPlan {name: COALESCE(row.`Subscription Plan`, 'Unknown Plan')})
MERGE (deviceNode:Device {name: COALESCE(row.`Devices Used`, 'Unknown Device')})
MERGE (person)-[:USES]->(deviceNode)

MERGE (person)-[:LIVES_IN]->(location)
MERGE (person)-[:SUBSCRIBED_TO]->(plan)
MERGE (person)-[:HAS_USER_ID]->(:UserID {id: COALESCE(row.`User ID`, 'Unknown ID')})
MERGE (person)-[:HAS_USERNAME]->(:Username {name: COALESCE(row.`Username`, 'Unknown Username')})
MERGE (person)-[:HAS_BIRTH_DATE]->(:BirthDate {date: COALESCE(row.`Date of Birth`, 'Unknown Date')})
MERGE (person)-[:HAS_GENDER]->(:Gender {type: COALESCE(row.`Gender`, 'Unknown Gender')})
MERGE (person)-[:MEMBERSHIP_STARTED_ON]->(:MembershipStartDate {date: COALESCE(row.`Membership Start Date`, 'Unknown Start Date')})
MERGE (person)-[:MEMBERSHIP_ENDED_ON]->(:MembershipEndDate {date: COALESCE(row.`Membership End Date`, 'Unknown End Date')})
MERGE (person)-[:HAS_PAYMENT_INFO]->(:PaymentInformation {info: COALESCE(row.`Payment Information`, 'Unknown Payment Info')})
MERGE (person)-[:HAS_RENEWAL_STATUS]->(:RenewalStatus {status: COALESCE(row.`Renewal Status`, 'Unknown Status')})
MERGE (person)-[:HAS_USAGE_FREQUENCY]->(:UsageFrequency {frequency: COALESCE(row.`Usage Frequency`, 'Unknown Frequency')})
MERGE (person)-[:HAS_PURCHASE_HISTORY]->(:PurchaseHistory {history: COALESCE(row.`Purchase History`, 'Unknown History')})
MERGE (person)-[:HAS_FAVORITE_GENRES]->(:FavoriteGenres {genres: COALESCE(row.`Favorite Genres`, 'Unknown Genres')})
MERGE (person)-[:HAS_ENGAGEMENT_METRICS]->(:EngagementMetrics {metrics: COALESCE(row.`Engagement Metrics`, 'Unknown Metrics')})
MERGE (person)-[:GAVE_FEEDBACK]->(:Feedback {ratings: COALESCE(row.`Feedback/Ratings`, 'No Feedback')})
MERGE (person)-[:INTERACTED_WITH_SUPPORT]->(:CustomerSupport {interactions: COALESCE(row.`Customer Support Interactions`, 'No Interactions')})

"""

graph.query(users_query)

def response_generation(query):
    chain = GraphCypherQAChain.from_llm(graph=graph, llm=llm, verbose=True)
    answer = chain.run(query+ f"return with proper naming conventions what you get as input rephrase it with this {user_query}")
    return answer

st.set_page_config(page_title="Knowledge Graph Chatbot", page_icon=":robot_face:")

st.markdown("""
<div style="text-align: center;">
    <h1 style="color: #0078D7;">Knowledge Graph Chatbot</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; font-size: 18px; color: #555;">
    A RAG chatbot created with langchain and knowledge graphs using llama3.</p>
""", unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

user_query = st.text_input("Enter your question:", placeholder="E.g., Which devices is uesd by Alice to watch shows?")

if st.button("Ask"):
    bot_response = response_generation(user_query)

    
    st.markdown(f"""
    <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px; margin-top: 20px;">
        <h4 style="color: #0078D7;">Answer :</h4>
        <p style="color: #333;">{bot_response}</p>
    </div>
    """, unsafe_allow_html=True)

