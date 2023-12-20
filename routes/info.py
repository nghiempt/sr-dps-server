from fastapi import APIRouter
from models._index import ResponseObject
import http.client as HTTP_STATUS_CODE

infoRouter = APIRouter(prefix="/api/v1")

@infoRouter.get('/info/get-project-info')
async def get_project_info():
    info = {
        "info_1" : "The project 'Privacy Policy Survey' is a web application designed with the goal of providing users with an intuitive platform to learn and evaluate mobile applications based on data security and privacy policies. private. This project includes two main pages: a category selection page and an app details page.",
        "sub_info_1" : "The 'Choose Category' page allows users to freely choose application categories according to their personal preferences. Once they have selected a specific category, they will be taken to the app details page. This details page shows detailed information about each app in the category, including the name, description, number of apps, and a review of the app's data security and privacy policy.",
        "sub_info_2" : "Besides, the application detail page also provides a table to check whether the application violates the information criteria (Incorrect, Incomplete, Inconsistent). Additionally, users have the opportunity to rate their personal opinion of each app based on their experience, by choosing from options such as 'strongly agree', 'agree', 'neutral', and many other options.",
        "info_2" : "The 'Privacy Policy Survey' project brings value to users by providing detailed information and reviews on data security and privacy policies of mobile applications, helping them make the right decisions It is correct and safe to use these applications."
    }
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, info)

@infoRouter.get('/info/get-concept-description')
async def get_project_info():
    info = {
        "incorrect" : "'Incorrect' is used to indicate that certain information or data is inaccurate, misleading, or untrue. 'Incorrect' information can include incorrect data about numbers, events, names, or any information that can be compared to the truth and judged to be inaccurate.",
        "incomplete" : "'Incomplete' implies that the information or data provided is not complete or an important part is missing. 'Incomplete' information can include leaving out important parts, not providing enough information to understand an issue, or not fully meeting a request.",
        "inconsistent" : "'Inconsistent' is when information or data has inconsistencies or contradictions in content. This can happen when pieces of information contradict each other or do not demonstrate consistency in context or logic. 'Inconsistent' information can lead to misunderstandings or conflicts in decisions or actions based on it."
        }
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, info)

@infoRouter.get('/info/get-google-exception')
async def get_project_info():
    info = {
        "data_shared" : [
            "The data is transferred to a third party based on a specific action that you initiate, where you reasonably expect the data to be shared.",
            "The data transfer to a third party is prominently disclosed in the app, and the app requests your consent.",
            "The data is transferred to a service provider to process it on the developer's behalf.",
            "The data is transferred for specific legal purposes.",
            "The data transferred is fully anonymised so it can no longer be associated with any individual."
        ],
        "data_collected" : [
            "An app accesses the data only on your device and it is not sent off your device.",
            "Your data is sent off the device but only processed ephemerally.",
            "Your data is sent using end-to-end encryption."
        ],
        "security_practices" : [
            "Encrypts data",
            "Provides a way for you to request that your data be deleted or automatically deletes or anonymises your data within 90 days."
        ],
        "references" : "Link exception: https://support.google.com/googleplay/answer/11416267?hl=vi&visit_id=638227555913177053-2754724865&p=data-safety&rd=1"
        }
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, info)

@infoRouter.get('/info/get-team-info')
async def get_project_info():
    info = {
        "team_name" : "Double N",
        "target" : "The team's goal is to develop and deploy a web application to provide insights into mobile applications based on data security and privacy policies. Main tasks include interface design, data analysis and website deployment.",
        "member" : [
            {
                "name" : "Pham Thanh Nghiem",
                "role" : "Leader",
                "avatar" : ""
            },
            {
                "name" : "Le Truc Nhi",
                "role" : "Member",
                "avatar" : ""   
            }
        ],
        "intended_target" : [
            "Complete website design and implementation within stated timeframe.",
            "Provide detailed information about data security and privacy policies to users.",
            "Collect reviews from users about mobile applications."
        ]
        }
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, info)

