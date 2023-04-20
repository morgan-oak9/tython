// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_compute_address.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.ComputeAddress {

  /// <summary>Holder for reflection information generated from gcp/gcp_compute_address.proto</summary>
  public static partial class GcpComputeAddressReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_compute_address.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpComputeAddressReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch1nY3AvZ2NwX2NvbXB1dGVfYWRkcmVzcy5wcm90bxIfb2FrOS50eXRob24u",
            "Z2NwLmNvbXB1dGVfYWRkcmVzcxoTc2hhcmVkL3NoYXJlZC5wcm90byI5ChdD",
            "b21wdXRlQWRkcmVzc1hUaW1lb3V0cxIOCgZjcmVhdGUYASABKAkSDgoGZGVs",
            "ZXRlGAIgASgJIq0DCg5Db21wdXRlQWRkcmVzcxIPCgdhZGRyZXNzGAEgASgJ",
            "EhQKDGFkZHJlc3NfdHlwZRgCIAEoCRIaChJjcmVhdGlvbl90aW1lc3RhbXAY",
            "AyABKAkSEwoLZGVzY3JpcHRpb24YBCABKAkSCgoCaWQYBSABKAkSDAoEbmFt",
            "ZRgGIAEoCRIPCgduZXR3b3JrGAcgASgJEhQKDG5ldHdvcmtfdGllchgIIAEo",
            "CRIVCg1wcmVmaXhfbGVuZ3RoGAkgASgBEg8KB3Byb2plY3QYCiABKAkSDwoH",
            "cHVycG9zZRgLIAEoCRIOCgZyZWdpb24YDCABKAkSEQoJc2VsZl9saW5rGA0g",
            "ASgJEhIKCnN1Ym5ldHdvcmsYDiABKAkSDQoFdXNlcnMYDyADKAkSSgoIdGlt",
            "ZW91dHMYECABKAsyOC5vYWs5LnR5dGhvbi5nY3AuY29tcHV0ZV9hZGRyZXNz",
            "LkNvbXB1dGVBZGRyZXNzWFRpbWVvdXRzEjcKDXJlc291cmNlX2luZm8YESAB",
            "KAsyIC5vYWs5LnR5dGhvbi5zaGFyZWQuUmVzb3VyY2VJbmZvYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts), global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts.Parser, new[]{ "Create", "Delete" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddress), global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddress.Parser, new[]{ "Address", "AddressType", "CreationTimestamp", "Description", "Id", "Name", "Network", "NetworkTier", "PrefixLength", "Project", "Purpose", "Region", "SelfLink", "Subnetwork", "Users", "Timeouts", "ResourceInfo" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class ComputeAddressXTimeouts : pb::IMessage<ComputeAddressXTimeouts>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ComputeAddressXTimeouts> _parser = new pb::MessageParser<ComputeAddressXTimeouts>(() => new ComputeAddressXTimeouts());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ComputeAddressXTimeouts> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.ComputeAddress.GcpComputeAddressReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeAddressXTimeouts() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeAddressXTimeouts(ComputeAddressXTimeouts other) : this() {
      create_ = other.create_;
      delete_ = other.delete_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeAddressXTimeouts Clone() {
      return new ComputeAddressXTimeouts(this);
    }

    /// <summary>Field number for the "create" field.</summary>
    public const int CreateFieldNumber = 1;
    private string create_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Create {
      get { return create_; }
      set {
        create_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "delete" field.</summary>
    public const int DeleteFieldNumber = 2;
    private string delete_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Delete {
      get { return delete_; }
      set {
        delete_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ComputeAddressXTimeouts);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ComputeAddressXTimeouts other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Create != other.Create) return false;
      if (Delete != other.Delete) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Create.Length != 0) hash ^= Create.GetHashCode();
      if (Delete.Length != 0) hash ^= Delete.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Create.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Create);
      }
      if (Delete.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(Delete);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Create.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Create);
      }
      if (Delete.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Delete);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ComputeAddressXTimeouts other) {
      if (other == null) {
        return;
      }
      if (other.Create.Length != 0) {
        Create = other.Create;
      }
      if (other.Delete.Length != 0) {
        Delete = other.Delete;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Create = input.ReadString();
            break;
          }
          case 18: {
            Delete = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class ComputeAddress : pb::IMessage<ComputeAddress>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<ComputeAddress> _parser = new pb::MessageParser<ComputeAddress>(() => new ComputeAddress());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<ComputeAddress> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.ComputeAddress.GcpComputeAddressReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeAddress() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeAddress(ComputeAddress other) : this() {
      address_ = other.address_;
      addressType_ = other.addressType_;
      creationTimestamp_ = other.creationTimestamp_;
      description_ = other.description_;
      id_ = other.id_;
      name_ = other.name_;
      network_ = other.network_;
      networkTier_ = other.networkTier_;
      prefixLength_ = other.prefixLength_;
      project_ = other.project_;
      purpose_ = other.purpose_;
      region_ = other.region_;
      selfLink_ = other.selfLink_;
      subnetwork_ = other.subnetwork_;
      users_ = other.users_.Clone();
      timeouts_ = other.timeouts_ != null ? other.timeouts_.Clone() : null;
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public ComputeAddress Clone() {
      return new ComputeAddress(this);
    }

    /// <summary>Field number for the "address" field.</summary>
    public const int AddressFieldNumber = 1;
    private string address_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Address {
      get { return address_; }
      set {
        address_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "address_type" field.</summary>
    public const int AddressTypeFieldNumber = 2;
    private string addressType_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string AddressType {
      get { return addressType_; }
      set {
        addressType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "creation_timestamp" field.</summary>
    public const int CreationTimestampFieldNumber = 3;
    private string creationTimestamp_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string CreationTimestamp {
      get { return creationTimestamp_; }
      set {
        creationTimestamp_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "description" field.</summary>
    public const int DescriptionFieldNumber = 4;
    private string description_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Description {
      get { return description_; }
      set {
        description_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "id" field.</summary>
    public const int IdFieldNumber = 5;
    private string id_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Id {
      get { return id_; }
      set {
        id_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 6;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "network" field.</summary>
    public const int NetworkFieldNumber = 7;
    private string network_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Network {
      get { return network_; }
      set {
        network_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "network_tier" field.</summary>
    public const int NetworkTierFieldNumber = 8;
    private string networkTier_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string NetworkTier {
      get { return networkTier_; }
      set {
        networkTier_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "prefix_length" field.</summary>
    public const int PrefixLengthFieldNumber = 9;
    private double prefixLength_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public double PrefixLength {
      get { return prefixLength_; }
      set {
        prefixLength_ = value;
      }
    }

    /// <summary>Field number for the "project" field.</summary>
    public const int ProjectFieldNumber = 10;
    private string project_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Project {
      get { return project_; }
      set {
        project_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "purpose" field.</summary>
    public const int PurposeFieldNumber = 11;
    private string purpose_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Purpose {
      get { return purpose_; }
      set {
        purpose_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "region" field.</summary>
    public const int RegionFieldNumber = 12;
    private string region_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Region {
      get { return region_; }
      set {
        region_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "self_link" field.</summary>
    public const int SelfLinkFieldNumber = 13;
    private string selfLink_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string SelfLink {
      get { return selfLink_; }
      set {
        selfLink_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "subnetwork" field.</summary>
    public const int SubnetworkFieldNumber = 14;
    private string subnetwork_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Subnetwork {
      get { return subnetwork_; }
      set {
        subnetwork_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "users" field.</summary>
    public const int UsersFieldNumber = 15;
    private static readonly pb::FieldCodec<string> _repeated_users_codec
        = pb::FieldCodec.ForString(122);
    private readonly pbc::RepeatedField<string> users_ = new pbc::RepeatedField<string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<string> Users {
      get { return users_; }
    }

    /// <summary>Field number for the "timeouts" field.</summary>
    public const int TimeoutsFieldNumber = 16;
    private global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts timeouts_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts Timeouts {
      get { return timeouts_; }
      set {
        timeouts_ = value;
      }
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 17;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as ComputeAddress);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(ComputeAddress other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Address != other.Address) return false;
      if (AddressType != other.AddressType) return false;
      if (CreationTimestamp != other.CreationTimestamp) return false;
      if (Description != other.Description) return false;
      if (Id != other.Id) return false;
      if (Name != other.Name) return false;
      if (Network != other.Network) return false;
      if (NetworkTier != other.NetworkTier) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.Equals(PrefixLength, other.PrefixLength)) return false;
      if (Project != other.Project) return false;
      if (Purpose != other.Purpose) return false;
      if (Region != other.Region) return false;
      if (SelfLink != other.SelfLink) return false;
      if (Subnetwork != other.Subnetwork) return false;
      if(!users_.Equals(other.users_)) return false;
      if (!object.Equals(Timeouts, other.Timeouts)) return false;
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Address.Length != 0) hash ^= Address.GetHashCode();
      if (AddressType.Length != 0) hash ^= AddressType.GetHashCode();
      if (CreationTimestamp.Length != 0) hash ^= CreationTimestamp.GetHashCode();
      if (Description.Length != 0) hash ^= Description.GetHashCode();
      if (Id.Length != 0) hash ^= Id.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (Network.Length != 0) hash ^= Network.GetHashCode();
      if (NetworkTier.Length != 0) hash ^= NetworkTier.GetHashCode();
      if (PrefixLength != 0D) hash ^= pbc::ProtobufEqualityComparers.BitwiseDoubleEqualityComparer.GetHashCode(PrefixLength);
      if (Project.Length != 0) hash ^= Project.GetHashCode();
      if (Purpose.Length != 0) hash ^= Purpose.GetHashCode();
      if (Region.Length != 0) hash ^= Region.GetHashCode();
      if (SelfLink.Length != 0) hash ^= SelfLink.GetHashCode();
      if (Subnetwork.Length != 0) hash ^= Subnetwork.GetHashCode();
      hash ^= users_.GetHashCode();
      if (timeouts_ != null) hash ^= Timeouts.GetHashCode();
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Address.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Address);
      }
      if (AddressType.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(AddressType);
      }
      if (CreationTimestamp.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(CreationTimestamp);
      }
      if (Description.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Description);
      }
      if (Id.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Id);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Name);
      }
      if (Network.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(Network);
      }
      if (NetworkTier.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(NetworkTier);
      }
      if (PrefixLength != 0D) {
        output.WriteRawTag(73);
        output.WriteDouble(PrefixLength);
      }
      if (Project.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(Project);
      }
      if (Purpose.Length != 0) {
        output.WriteRawTag(90);
        output.WriteString(Purpose);
      }
      if (Region.Length != 0) {
        output.WriteRawTag(98);
        output.WriteString(Region);
      }
      if (SelfLink.Length != 0) {
        output.WriteRawTag(106);
        output.WriteString(SelfLink);
      }
      if (Subnetwork.Length != 0) {
        output.WriteRawTag(114);
        output.WriteString(Subnetwork);
      }
      users_.WriteTo(output, _repeated_users_codec);
      if (timeouts_ != null) {
        output.WriteRawTag(130, 1);
        output.WriteMessage(Timeouts);
      }
      if (resourceInfo_ != null) {
        output.WriteRawTag(138, 1);
        output.WriteMessage(ResourceInfo);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Address.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Address);
      }
      if (AddressType.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(AddressType);
      }
      if (CreationTimestamp.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(CreationTimestamp);
      }
      if (Description.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Description);
      }
      if (Id.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(Id);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(50);
        output.WriteString(Name);
      }
      if (Network.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(Network);
      }
      if (NetworkTier.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(NetworkTier);
      }
      if (PrefixLength != 0D) {
        output.WriteRawTag(73);
        output.WriteDouble(PrefixLength);
      }
      if (Project.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(Project);
      }
      if (Purpose.Length != 0) {
        output.WriteRawTag(90);
        output.WriteString(Purpose);
      }
      if (Region.Length != 0) {
        output.WriteRawTag(98);
        output.WriteString(Region);
      }
      if (SelfLink.Length != 0) {
        output.WriteRawTag(106);
        output.WriteString(SelfLink);
      }
      if (Subnetwork.Length != 0) {
        output.WriteRawTag(114);
        output.WriteString(Subnetwork);
      }
      users_.WriteTo(ref output, _repeated_users_codec);
      if (timeouts_ != null) {
        output.WriteRawTag(130, 1);
        output.WriteMessage(Timeouts);
      }
      if (resourceInfo_ != null) {
        output.WriteRawTag(138, 1);
        output.WriteMessage(ResourceInfo);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Address.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Address);
      }
      if (AddressType.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(AddressType);
      }
      if (CreationTimestamp.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(CreationTimestamp);
      }
      if (Description.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Description);
      }
      if (Id.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Id);
      }
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (Network.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Network);
      }
      if (NetworkTier.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(NetworkTier);
      }
      if (PrefixLength != 0D) {
        size += 1 + 8;
      }
      if (Project.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Project);
      }
      if (Purpose.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Purpose);
      }
      if (Region.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Region);
      }
      if (SelfLink.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SelfLink);
      }
      if (Subnetwork.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Subnetwork);
      }
      size += users_.CalculateSize(_repeated_users_codec);
      if (timeouts_ != null) {
        size += 2 + pb::CodedOutputStream.ComputeMessageSize(Timeouts);
      }
      if (resourceInfo_ != null) {
        size += 2 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(ComputeAddress other) {
      if (other == null) {
        return;
      }
      if (other.Address.Length != 0) {
        Address = other.Address;
      }
      if (other.AddressType.Length != 0) {
        AddressType = other.AddressType;
      }
      if (other.CreationTimestamp.Length != 0) {
        CreationTimestamp = other.CreationTimestamp;
      }
      if (other.Description.Length != 0) {
        Description = other.Description;
      }
      if (other.Id.Length != 0) {
        Id = other.Id;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      if (other.Network.Length != 0) {
        Network = other.Network;
      }
      if (other.NetworkTier.Length != 0) {
        NetworkTier = other.NetworkTier;
      }
      if (other.PrefixLength != 0D) {
        PrefixLength = other.PrefixLength;
      }
      if (other.Project.Length != 0) {
        Project = other.Project;
      }
      if (other.Purpose.Length != 0) {
        Purpose = other.Purpose;
      }
      if (other.Region.Length != 0) {
        Region = other.Region;
      }
      if (other.SelfLink.Length != 0) {
        SelfLink = other.SelfLink;
      }
      if (other.Subnetwork.Length != 0) {
        Subnetwork = other.Subnetwork;
      }
      users_.Add(other.users_);
      if (other.timeouts_ != null) {
        if (timeouts_ == null) {
          Timeouts = new global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts();
        }
        Timeouts.MergeFrom(other.Timeouts);
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Address = input.ReadString();
            break;
          }
          case 18: {
            AddressType = input.ReadString();
            break;
          }
          case 26: {
            CreationTimestamp = input.ReadString();
            break;
          }
          case 34: {
            Description = input.ReadString();
            break;
          }
          case 42: {
            Id = input.ReadString();
            break;
          }
          case 50: {
            Name = input.ReadString();
            break;
          }
          case 58: {
            Network = input.ReadString();
            break;
          }
          case 66: {
            NetworkTier = input.ReadString();
            break;
          }
          case 73: {
            PrefixLength = input.ReadDouble();
            break;
          }
          case 82: {
            Project = input.ReadString();
            break;
          }
          case 90: {
            Purpose = input.ReadString();
            break;
          }
          case 98: {
            Region = input.ReadString();
            break;
          }
          case 106: {
            SelfLink = input.ReadString();
            break;
          }
          case 114: {
            Subnetwork = input.ReadString();
            break;
          }
          case 122: {
            users_.AddEntriesFrom(input, _repeated_users_codec);
            break;
          }
          case 130: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 138: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            Address = input.ReadString();
            break;
          }
          case 18: {
            AddressType = input.ReadString();
            break;
          }
          case 26: {
            CreationTimestamp = input.ReadString();
            break;
          }
          case 34: {
            Description = input.ReadString();
            break;
          }
          case 42: {
            Id = input.ReadString();
            break;
          }
          case 50: {
            Name = input.ReadString();
            break;
          }
          case 58: {
            Network = input.ReadString();
            break;
          }
          case 66: {
            NetworkTier = input.ReadString();
            break;
          }
          case 73: {
            PrefixLength = input.ReadDouble();
            break;
          }
          case 82: {
            Project = input.ReadString();
            break;
          }
          case 90: {
            Purpose = input.ReadString();
            break;
          }
          case 98: {
            Region = input.ReadString();
            break;
          }
          case 106: {
            SelfLink = input.ReadString();
            break;
          }
          case 114: {
            Subnetwork = input.ReadString();
            break;
          }
          case 122: {
            users_.AddEntriesFrom(ref input, _repeated_users_codec);
            break;
          }
          case 130: {
            if (timeouts_ == null) {
              Timeouts = new global::Oak9.Tython.Gcp.ComputeAddress.ComputeAddressXTimeouts();
            }
            input.ReadMessage(Timeouts);
            break;
          }
          case 138: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
