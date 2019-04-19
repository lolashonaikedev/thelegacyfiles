using UnityEngine;
using System.Collections;
//using System;
//Tracks the Stylus and draws it to the screen using a Line Renderer
public class StylusScript : MonoBehaviour {

	private ZSCore _zsCore;
	//set the stylus as the tracker target type
	private ZSCore.TrackerTargetType _targetType = ZSCore.TrackerTargetType.Primary;
	private LineRenderer lr;
	private Vector3 _projectionPoint;
	private const float _camRayLength = 100.0f;
	//For the Colliding and Picking Up Stylus Script
	private GameObject collideObj; //to find the colliding gameObject
	private RaycastHit rayHit; //to find where the rayHits it
	private float distance;
	private Vector3 posObj;
	public void Start(){
		_zsCore = GameObject.Find ("ZSCore").GetComponent<ZSCore> ();
		_zsCore.Updated += new ZSCore.CoreEventHandler (OnCoreUpdated);
		lr = GetComponent<LineRenderer> ();

		}
	// The Location on screen that the stylus is pointing to
	/*public Vector3 GetPointerLocation () {
		return _projectionPoint;
		}*/
	//The location on the screen that the Stylus is pointing to
	private void OnCoreUpdated (ZSCore sender){
		UpdateStylusPose ();
		UpdateProjectionPoint ();
		DrawStylusBeam ();
	}
	private void UpdateStylusPose () {
				Matrix4x4 pose = _zsCore.GetTrackerTargetWorldPose (_targetType);
				transform.position = new Vector3 (pose.m03  , 
		                                 pose.m13 ,
		                                 pose.m23 );
				transform.rotation = Quaternion.LookRotation (pose.GetColumn (2), pose.GetColumn (1));
		}
	private void UpdateProjectionPoint (){
		RaycastHit hit_;
		if (Physics.Raycast (transform.position, transform.forward, out hit_, _camRayLength)){
						_projectionPoint = hit_.point;
				}
		else {
			Ray ray = new Ray(transform.position, transform.forward);
			_projectionPoint = ray.GetPoint (_camRayLength);
				}
	}
    private void DrawStylusBeam()
	{
		lr.SetPosition (0, transform.position);
		lr.SetPosition (1, _projectionPoint);
	}
	void Update(){
		if (_zsCore.IsTrackerTargetButtonPressed (ZSCore.TrackerTargetType.Primary, 0)){
			var ray = new Ray(transform.position, transform.forward);
			var hit=Physics.Raycast(ray.origin, ray.direction, out rayHit);
		if (hit){
				collideObj = rayHit.collider.gameObject;
				distance = rayHit.distance;
				Debug.Log (collideObj.name);
				Debug.Log ("I hit the clouds");
			}
			posObj = ray.origin+distance*ray.direction;
			collideObj.transform.position = new Vector3(posObj.x,posObj.y, posObj.z);
		}





		}
	/*
	void buttonHandler(){
		bool button0 = _zsCore.IsTrackerTargetButtonPressed (_targetType, 0);
		if (button0) {
			if (currentState [0] == false){
				//because the this script is attached to the stylus transform here is the transform of the stylus
				points.transform.parent = transform;
			}
			currentState [0] = true;
		} else {
			if (currentState [0] == true){
				//pointsParent is another GameObject that stores the points GameObject and lets me store another transform to use as a parent 
				points.transform.parent = pointsParent.transform;
			}
			currentState [0] = false;
		}
	/*
	private LineRenderer lr;
	
	public GameObject contactPoint;
	
	private Quaternion initialRotation = new Quaternion();
	private Vector3 initialPosition = new Vector3();
	private ZSCore _zsCore;
	private ZSCore.TrackerTargetType _targetType = ZSCore.TrackerTargetType.Primary;
	
	public void Start ()
	{
		_zsCore = GameObject.Find ("ZSCore").GetComponent<ZSCore> ();
		_zsCore.Updated += new ZSCore.CoreEventHandler (OnCoreUpdated);
		initialRotation = transform.rotation;
		initialPosition = transform.position;
		
		contactPoint = GameObject.Find("ContactPoint");
		contactPoint.SetActive(false);
		
		lr = GetComponent<LineRenderer>();
	}

	public void Update(){
		RaycastHit hit;
		if (Physics.Raycast (transform.position,
		                     transform.forward,
		                     out hit)){
			lr.SetPosition(0,hit.point);
			lr.SetPosition(1,transform.position);
			contactPoint.SetActive(true);
			contactPoint.transform.position = hit.point;
		}
		else{
			lr.SetPosition(0,(transform.position
			                  +transform.forward)*10f);
			lr.SetPosition(1,transform.position);
			contactPoint.SetActive(false);
		}
	}
	
	/// called by ZSCore after each input update.
	private void OnCoreUpdated (ZSCore sender)
	{
		UpdateStylusPose ();
	}		
	
	private void UpdateStylusPose ()
	{
		Matrix4x4 pose = _zsCore.GetTrackerTargetWorldPose (_targetType);
		transform.position = new Vector3 (pose.m03 + initialPosition.x,
		                                  pose.m13 + initialPosition.y,
		                                  pose.m23 + initialPosition.z);
		transform.rotation = Quaternion.LookRotation(pose.GetColumn(2), pose.GetColumn(1))
			* initialRotation;
	}
*/
}
